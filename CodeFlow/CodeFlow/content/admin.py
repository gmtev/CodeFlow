from django.contrib import admin
from CodeFlow.content.models import Question, Lecture


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_title', 'slug', 'author', 'created_at', 'is_answered')
    search_fields = ('question_title', 'author', 'is_answered')
    ordering = ('pk', 'author', 'created_at', 'is_answered')
    readonly_fields = ('slug',)


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('lecture_title', 'slug', 'author',)
    search_fields = ('lecture_title', 'author')
    ordering = ('pk', 'author')
    readonly_fields = ('slug',)