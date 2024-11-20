from django.contrib.auth import get_user_model
from django.db import models
from CodeFlow.content.models import Question
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

UserModel = get_user_model()


class Comment(models.Model):
    COMMENT_MAX_LENGTH = 500
    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]
        ordering = ['-created_at']
    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        'content_type', 'object_id'
    )
    content = models.TextField(
        max_length=COMMENT_MAX_LENGTH
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Comment by {self.user} on {self.content_object}"

class Like(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        'content_type', 'object_id'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Like by {self.user} on {self.content_object}"
