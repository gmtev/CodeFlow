from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from CodeFlow.accounts.models import Profile
from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ValidationError
UserModel = get_user_model()


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove or customize help text for password fields
        self.fields['password1'].help_text = "At least 8 characters, not too common and not entirely numeric."
        self.fields['password2'].help_text = None


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )


    def clean_profile_picture(self):
        file = self.cleaned_data.get('profile_picture')

        if file:
            if isinstance(file, UploadedFile):  # Check if file is an UploadedFile instance
                if file.size > 5 * 1024 * 1024:  # Convert 10 MB to bytes
                    raise ValidationError("File shouldn't be larger than 5MB.")

        return file
