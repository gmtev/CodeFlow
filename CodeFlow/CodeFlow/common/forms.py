from django import forms
from CodeFlow.common.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
