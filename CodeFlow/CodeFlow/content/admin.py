from django.contrib import admin
from CodeFlow.content.models import Question, Lecture


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_at', 'is_answered')
    search_fields = ('title', 'author', 'is_answered')
    ordering = ('pk', 'author', 'created_at', 'is_answered')
    readonly_fields = ('slug',)


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_at')
    search_fields = ('title', 'author')
    ordering = ('pk', 'author', 'created_at')
    readonly_fields = ('slug',)