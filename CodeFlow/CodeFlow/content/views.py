from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from CodeFlow.commons.models import Comment, Like
from CodeFlow.content.forms import QuestionEditForm, QuestionCreateForm, QuestionDeleteForm
from CodeFlow.content.forms import LectureCreateForm, LectureDeleteForm, LectureEditForm
from CodeFlow.commons.forms import CommentForm
from CodeFlow.content.models import Question, Lecture
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class QuestionListView(ListView):
    model = Question
    template_name = 'content/questions.html'
    context_object_name = 'questions'
    # paginate_by = 5

# class QuestionDetailView(LoginRequiredMixin, DetailView):
#     model = Question
#     template_name = 'content/question-details-page.html'
#     slug_url_kwarg = 'slug'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comment_form'] = CommentForm()
#
#         return context

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'content/question-details-page.html'
    context_object_name = 'question'
    slug_url_kwarg = 'slug'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.object
        question_content_type = ContentType.objects.get_for_model(Question)
        likes = Like.objects.filter(content_type=question_content_type, object_id=question.id)
        comments = Comment.objects.filter(content_type=question_content_type, object_id=question.id)
        user_has_liked = likes.filter(user=self.request.user).exists() if self.request.user.is_authenticated else False
        context['likes'] = likes
        context['comments'] = comments
        context['user_has_liked'] = user_has_liked
        context['comment_form'] = CommentForm()
        return context

class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionCreateForm
    template_name = 'content/question-create-page.html'
    success_url = reverse_lazy('questions')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    template_name = 'content/question-edit-page.html'
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
    template_name = 'content/question-delete-page.html'
    slug_url_kwarg = 'slug'
    form_class = QuestionDeleteForm

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.request.user.pk,
            }
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
    template_name = 'content/lectures.html'
    context_object_name = 'lectures'
    # paginate_by = 5

class LectureDetailView(LoginRequiredMixin, DetailView):
    model = Lecture
    template_name = 'content/lecture-details-page.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lecture = self.object
        lecture_content_type = ContentType.objects.get_for_model(Lecture)
        likes = Like.objects.filter(content_type=lecture_content_type, object_id=lecture.id)
        comments = Comment.objects.filter(content_type=lecture_content_type, object_id=lecture.id)
        user_has_liked = likes.filter(user=self.request.user).exists() if self.request.user.is_authenticated else False
        context['likes'] = likes
        context['comments'] = comments
        context['user_has_liked'] = user_has_liked
        context['comment_form'] = CommentForm()
        return context

class LectureCreateView(CreateView):
    model = Lecture
    form_class = LectureCreateForm
    template_name = 'content/lecture-create-page.html'
    success_url = reverse_lazy('lectures')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class LectureEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lecture
    template_name = 'content/lecture-edit-page.html'
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
    template_name = 'content/lecture-delete-page.html'
    slug_url_kwarg = 'slug'
    form_class = LectureDeleteForm

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.request.user.pk,
            }
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