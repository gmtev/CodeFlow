from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from CodeFlow.content.models import Question, Lecture


class QuestionAndLectureModelsTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123"
        )

    def test_question_title_length_validation(self):
        question = Question(
            title="A",
            text="This is a sample question.",
            author=self.user
        )
        with self.assertRaises(ValidationError):
            question.full_clean()

        question.title = "A" * (Question.MAX_TITLE_SIZE + 1)
        with self.assertRaises(ValidationError):
            question.full_clean()

        question.title = "Valid Title"
        try:
            question.full_clean()
        except ValidationError:
            self.fail("ValidationError raised unexpectedly for a valid title.")

    def test_lecture_title_length_validation(self):
        lecture = Lecture(
            title="A",
            text="This is a sample lecture.",
            author=self.user
        )
        with self.assertRaises(ValidationError):
            lecture.full_clean()

        lecture.title = "A" * (Lecture.MAX_TITLE_SIZE + 1)
        with self.assertRaises(ValidationError):
            lecture.full_clean()

        lecture.title = "Valid Title"
        try:
            lecture.full_clean()
        except ValidationError:
            self.fail("ValidationError raised unexpectedly for a valid title.")

    def test_question_title_custom_validator(self):
        question = Question(
            title="Invalid@Title!",
            text="This is a sample question.",
            author=self.user
        )
        try:
            question.full_clean()
        except ValidationError:
            self.fail("ValidationError raised unexpectedly for a valid title.")

        question.title = "Invalid*Title{"
        with self.assertRaises(ValidationError):
            question.full_clean()

    def test_lecture_title_custom_validator(self):
        lecture = Lecture(
            title="Valid-Title!",
            text="This is a sample lecture.",
            author=self.user
        )
        try:
            lecture.full_clean()
        except ValidationError:
            self.fail("ValidationError raised unexpectedly for a valid title.")

        lecture.title = "Invalid/Title{"
        with self.assertRaises(ValidationError):
            lecture.full_clean()

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

    def test_question_slug_generation(self):
        question = Question(
            title="Test question title",
            text="This is a test question.",
            author=self.user
        )
        question.save()
        self.assertTrue(question.slug)
        self.assertTrue(question.slug.startswith("test-question-title"))

    def test_question_ordering(self):
        question1 = Question(
            title="Question 1",
            text="This is the first question.",
            author=self.user
        )
        question1.save()

        question2 = Question(
            title="Question 2",
            text="This is the second question.",
            author=self.user
        )
        question2.save()

        questions = Question.objects.all()
        # since the Question model is ordered by "created_at" in descending order
        self.assertEqual(questions[0], question2)
        self.assertEqual(questions[1], question1)

    def test_lecture_slug_generation(self):
        lecture = Lecture(
            title="Test lecture title",
            text="This is a test lecture.",
            author=self.user
        )
        lecture.save()
        self.assertTrue(lecture.slug)
        self.assertTrue(lecture.slug.startswith("test-lecture-title"))