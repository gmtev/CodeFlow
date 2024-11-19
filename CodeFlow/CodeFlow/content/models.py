from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MinLengthValidator
from CodeFlow.validators import ImageSizeValidator

UserModel = get_user_model()


class Question(models.Model):
    MAX_QUESTION_IMAGE_SIZE = 5
    MIN_QUESTION_TITLE_SIZE = 5
    MAX_QUESTION_TITLE_SIZE = 100

    question_title = models.CharField(
        max_length=MAX_QUESTION_TITLE_SIZE,
        validators=[MinLengthValidator(MIN_QUESTION_TITLE_SIZE)],
    )

    text = models.TextField()
    profile_picture = models.ImageField(
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

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.question_title}-{self.id}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question_title