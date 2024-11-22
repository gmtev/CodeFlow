from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MinLengthValidator
from CodeFlow.validators import ImageSizeValidator, TitleValidator

UserModel = get_user_model()


class Question(models.Model):
    MAX_QUESTION_IMAGE_SIZE = 5
    MIN_QUESTION_TITLE_SIZE = 5
    MAX_QUESTION_TITLE_SIZE = 100

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]
        ordering = ['-created_at']

    question_title = models.CharField(
        max_length=MAX_QUESTION_TITLE_SIZE,
        validators=[
            MinLengthValidator(MIN_QUESTION_TITLE_SIZE),
            TitleValidator()
        ],
    )

    text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='',
        validators=[
            ImageSizeValidator(MAX_QUESTION_IMAGE_SIZE),
        ],
    )
    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
        editable=False,
    )

    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.question_title}-{self.id}")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.question_title} by {self.author}."


class Lecture(models.Model):
    MIN_LECTURE_TITLE_SIZE = 5
    MAX_LECTURE_TITLE_SIZE = 50

    class Meta:
        indexes = [
            models.Index(fields=['author']),
        ]
        ordering = ['author']

    lecture_title = models.CharField(
        max_length=MAX_LECTURE_TITLE_SIZE,
        validators=[
            MinLengthValidator(MIN_LECTURE_TITLE_SIZE),
            TitleValidator()
        ],
    )
    text = models.TextField()

    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.lecture_title} by {self.author}."

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.lecture_title}-{self.pk}")

        super().save(*args, **kwargs)
