from django.contrib import admin
from CodeFlow.commons.models import Like, Comment
# Register your models here.
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_type', 'object_id', 'created_at')
    search_fields = ('user', 'content_type', 'object_id')
    ordering = ('user', 'content_type', 'object_id', 'created_at')
    list_filter = ('user',)
    readonly_fields = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content_type', 'object_id', 'created_at', 'content')
    search_fields = ('author', 'content_type', 'object_id', 'created_at', 'content')
    ordering = ('author', 'content_type', 'object_id', 'created_at', 'content')
    list_filter = ('author',)
    readonly_fields = ('created_at',)