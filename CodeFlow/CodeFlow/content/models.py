from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MinLengthValidator
from CodeFlow.validators import ImageSizeValidator, TitleValidator

UserModel = get_user_model()


class BaseContent(models.Model):

    class Meta:
        abstract = True

    MIN_TITLE_SIZE = 5
    MAX_TITLE_SIZE = 100
    title = models.CharField(
        max_length=MAX_TITLE_SIZE,
        validators=[
            MinLengthValidator(MIN_TITLE_SIZE),
            TitleValidator(),
        ],
    )
    text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        editable=False,
    )
    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.title[:50]}-{self.id}")
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author}."


class Question(BaseContent):
    MAX_QUESTION_IMAGE_SIZE = 5

    class Meta(BaseContent.Meta):
        indexes = [
            models.Index(fields=['created_at']),
        ]
        ordering = ['-created_at']

    picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='',
        validators=[
            ImageSizeValidator(MAX_QUESTION_IMAGE_SIZE),
        ],
    )

    is_answered = models.BooleanField(
        default=False,
    )



class Lecture(BaseContent):

    class Meta(BaseContent.Meta):
        indexes = [
            models.Index(fields=['author']),
        ]
        ordering = ['author']


class Section(models.Model):
    MIN_SECTION_NAME_SIZE = 5
    MAX_SECTION_NAME_SIZE = 70

    section_name = models.CharField(
        max_length=MAX_SECTION_NAME_SIZE,
        validators=[
            MinLengthValidator(MIN_SECTION_NAME_SIZE),
            TitleValidator(),
        ],
    )
    text = models.TextField()

    lecture = models.ForeignKey(
        to=Lecture,
        on_delete=models.CASCADE,
        related_name="sections",
    )

    def __str__(self):
        return f"Point: {self.section_name} for Lecture: {self.lecture.title}"