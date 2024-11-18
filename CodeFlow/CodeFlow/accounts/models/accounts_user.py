from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MinLengthValidator
from CodeFlow.accounts.managers import CustomUserManager
from CodeFlow.validators import UsernameValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    MIN_LEN_USERNAME = 4
    MAX_LEN_USERNAME = 30
    username = models.CharField(
        unique=True,
        max_length=MAX_LEN_USERNAME,
        validators=[
            UsernameValidator(),
            MinLengthValidator(MIN_LEN_USERNAME),
        ],
    )
    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()