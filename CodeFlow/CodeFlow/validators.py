from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ImageSizeValidator:
    def __init__(self, file_size_mb: int, message=None):
        self.file_size_mb = file_size_mb
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"Image size must be below or equal to {self.file_size_mb}MB"
        else:
            self.__message = value

    def __call__(self, value):
        if value.size > self.file_size_mb * 1024 * 1024:
            raise ValidationError(self.message)


@deconstructible
class NameLetterValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must contain letters only!"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class UsernameValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = ('Username must contain only letters, digits, and the following characters:'
                              '(_, -, ., @)!')
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        for ch in value:
            if not ch.isalnum() and ch not in ['_', '-', '.', '@']:
                raise ValidationError(self.message)