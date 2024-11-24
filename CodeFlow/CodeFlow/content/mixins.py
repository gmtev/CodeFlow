from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from CodeFlow.content.models import Section

class SectionAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        section = get_object_or_404(Section, id=self.kwargs['pk'])
        return self.request.user == section.lecture.author
