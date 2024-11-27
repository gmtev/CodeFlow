from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from CodeFlow.commons.models import Comment, Like
from CodeFlow.content.forms import QuestionEditForm, QuestionCreateForm, QuestionDeleteForm
from CodeFlow.content.forms import LectureCreateForm, LectureDeleteForm, LectureEditForm
from CodeFlow.content.forms import SectionCreateForm, SectionEditForm
from CodeFlow.commons.forms import CommentForm
from CodeFlow.content.models import Question, Lecture, Section
from CodeFlow.content.mixins import SectionAuthorMixin

class QuestionListView(ListView):
    model = Question
    template_name = 'content/questions/questions.html'
    context_object_name = 'questions'
    paginate_by = 3


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'content/questions/question-details-page.html'
    context_object_name = 'question'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.object
        question_content_type = ContentType.objects.get_for_model(Question)
        likes = Like.objects.filter(content_type=question_content_type, object_id=question.id)
        all_comments = Comment.objects.filter(content_type=question_content_type, object_id=question.id)

        paginator = Paginator(all_comments, 5)
        page = self.request.GET.get('page')
        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)
        user_has_liked = likes.filter(user=self.request.user).exists() if self.request.user.is_authenticated else False
        context['is_paginated'] = comments.has_other_pages()
        context['page_obj'] = comments
        context['likes'] = likes
        context['comments'] = comments
        context['user_has_liked'] = user_has_liked
        context['comment_form'] = CommentForm()
        return context

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionCreateForm
    template_name = 'content/questions/question-create-page.html'
    success_url = reverse_lazy('questions')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    template_name = 'content/questions/question-edit-page.html'
    form_class = QuestionEditForm
    slug_url_kwarg = 'slug'

    def test_func(self):
        question = get_object_or_404(Question, slug=self.kwargs['slug'])
        return self.request.user == question.author


    def get_success_url(self):
        return reverse_lazy(
            'question-details',
            kwargs={
                'slug': self.kwargs['slug'],
            }
        )

class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    template_name = 'content/questions/question-delete-page.html'
    slug_url_kwarg = 'slug'
    form_class = QuestionDeleteForm

    def get_success_url(self):
        return reverse_lazy(
            'questions'
        )

    def test_func(self):
        question = get_object_or_404(Question, slug=self.kwargs['slug'])
        return self.request.user == question.author

    def get_initial(self) -> dict:
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs

class LectureListView(ListView):
    model = Lecture
    template_name = 'content/lectures/lectures.html'
    context_object_name = 'lectures'
    paginate_by = 4

class LectureDetailView(LoginRequiredMixin, DetailView):
    model = Lecture
    template_name = 'content/lectures/lecture-details-page.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lecture = self.object
        sections = lecture.sections.all()
        lecture_content_type = ContentType.objects.get_for_model(Lecture)
        likes = Like.objects.filter(content_type=lecture_content_type, object_id=lecture.id)
        comments = Comment.objects.filter(content_type=lecture_content_type, object_id=lecture.id)
        user_has_liked = likes.filter(user=self.request.user).exists() if self.request.user.is_authenticated else False
        context['sections'] = sections
        context['likes'] = likes
        context['comments'] = comments
        context['user_has_liked'] = user_has_liked
        context['comment_form'] = CommentForm()
        return context

class LectureCreateView(LoginRequiredMixin, CreateView):
    model = Lecture
    form_class = LectureCreateForm
    template_name = 'content/lectures/lecture-create-page.html'
    success_url = reverse_lazy('lectures')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class LectureEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lecture
    template_name = 'content/lectures/lecture-edit-page.html'
    form_class = LectureEditForm
    slug_url_kwarg = 'slug'

    def test_func(self):
        lecture = get_object_or_404(Lecture, slug=self.kwargs['slug'])
        return self.request.user == lecture.author

    def get_success_url(self):
        return reverse_lazy(
            'lecture-details',
            kwargs={
                'slug': self.kwargs['slug'],
            }
        )

class LectureDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lecture
    template_name = 'content/lectures/lecture-delete-page.html'
    slug_url_kwarg = 'slug'
    form_class = LectureDeleteForm

    def get_success_url(self):
        return reverse_lazy(
            'lectures'
        )

    def test_func(self):
        lecture = get_object_or_404(Lecture, slug=self.kwargs['slug'])
        return self.request.user == lecture.author

    def get_initial(self) -> dict:
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs


class SectionCreateView(LoginRequiredMixin, CreateView):
    model = Section
    form_class = SectionCreateForm
    template_name = "content/sections/section-create-page.html"

    def form_valid(self, form):
        lecture = get_object_or_404(Lecture, slug=self.kwargs['slug'])
        form.instance.lecture = lecture

        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        lecture = get_object_or_404(Lecture, slug=self.kwargs['slug'])
        if lecture.author != request.user:
            raise PermissionDenied
        self.lecture = lecture

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lecture'] = self.lecture

        return context

    def get_success_url(self):
        return reverse_lazy("lecture-details", kwargs={"slug": self.kwargs['slug']})



class SectionEditView(LoginRequiredMixin, SectionAuthorMixin, UpdateView):
    model = Section
    form_class = SectionEditForm
    template_name = "content/sections/section-edit-page.html"

    def get_success_url(self):
        lecture = self.object.lecture
        return reverse_lazy("lecture-details", kwargs={"slug": lecture.slug})


class SectionDeleteView(LoginRequiredMixin, SectionAuthorMixin, DeleteView):
    model = Section
    template_name = "content/sections/section-delete-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = self.object
        return context

    def get_success_url(self):
        lecture = self.object.lecture
        return reverse_lazy("lecture-details", kwargs={"slug": lecture.slug})


class SectionDetailView(LoginRequiredMixin, DetailView):
    model = Section
    template_name = "content/sections/section-details-page.html"
    context_object_name = "section"

