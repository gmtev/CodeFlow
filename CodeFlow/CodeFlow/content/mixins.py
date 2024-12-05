from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from CodeFlow.content.models import Section, Lecture, Question

class SectionAuthorPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        section = get_object_or_404(Section, id=self.kwargs['pk'])
        return self.request.user == section.lecture.author

class LectureAuthorPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        lecture = get_object_or_404(Lecture, slug=self.kwargs['slug'])
        return self.request.user == lecture.author

class QuestionAuthorPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        question = get_object_or_404(Question, slug=self.kwargs['slug'])
        return self.request.user == question.author