from django.test import TestCase
from CodeFlow.common.models import Comment
from CodeFlow.common.forms import CommentForm


class CommentFormTests(TestCase):

    def test_form_renders_placeholder(self):
        form = CommentForm()
        self.assertIn('placeholder="Add a comment..."', str(form.as_p()))

    def test_form_valid_data(self):
        form = CommentForm(data={'content': 'This is a valid comment.'})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data_empty_content(self):
        form = CommentForm(data={'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

    def test_form_exceeds_max_length(self):
        long_content = "a" * (Comment.COMMENT_MAX_LENGTH + 1)
        form = CommentForm(data={'content': long_content})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)