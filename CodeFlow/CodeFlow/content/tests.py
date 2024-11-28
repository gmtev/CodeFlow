from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


from CodeFlow.content.forms import QuestionBaseForm
from CodeFlow.content.models import Question, Lecture, Section


class BaseContentTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuserr",
            password="pa1ssword123",
            email='email@test.com'
        )

    def test_title_length_validation(self):
        question = Question(
            title="Test",
            text="This is a test question.",
            author=self.user
        )
        with self.assertRaises(ValidationError):
            question.full_clean()

        question.title = "Valid Title"
        try:
            question.full_clean()
        except ValidationError:
            self.fail("ValidationError raised unexpectedly!")

    def test_slug_generation(self):
        question = Question(
            title="Test question title",
            text="This is a test question.",
            author=self.user
        )
        question.save()
        self.assertTrue(question.slug)
        self.assertTrue(question.slug.startswith("test-question-title"))


class QuestionTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuserr",
            password="pa1ssword123",
            email='email@test.com'
        )

    def test_picture(self):
        image_content = b"image content"
        small_image = SimpleUploadedFile("small_image.jpg", image_content, content_type="image/jpeg")

        form_data = {
            'title': 'Test Question',
            'text': 'This is a test question.',
            'picture': small_image
        }

        form = QuestionBaseForm(data=form_data)

        self.assertTrue(form.is_valid(), "Form should be valid with a small image")



class LectureTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username="testuserr",
            password="pa1ssword123",
            email='email@test.com'
        )

    def test_lecture_ordering(self):
        lecture1 = Lecture(
            title="Lecture 1",
            text="This is the first lecture.",
            author=self.user
        )
        lecture1.save()

        lecture2 = Lecture(
            title="Lecture 2",
            text="This is the second lecture.",
            author=self.user
        )
        lecture2.save()

        lectures = Lecture.objects.all()
        self.assertEqual(lectures[0], lecture1)
        self.assertEqual(lectures[1], lecture2)



