from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth import password_validation
from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ValidationError
from CodeFlow.accounts.models import Profile

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

        self.fields['password1'].help_text = "At least 8 characters, not too common and not entirely numeric."
        self.fields['password2'].help_text = None


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )


    def clean_profile_picture(self):
        file = self.cleaned_data.get('profile_picture')

        if file:
            if isinstance(file, UploadedFile):
                if file.size > 5 * 1024 * 1024:
                    raise ValidationError("File shouldn't be larger than 5MB.")

        return file

class CustomUserEditForm(forms.ModelForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter current password'}),
        required=True,
        label="Current Password",
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password (optional)'}),
        required=False,
        label="New Password",
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}),
        required=False,
        label="Confirm Password",
    )

    class Meta:
        model = UserModel
        fields = ["username", "email"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise forms.ValidationError("The current password is incorrect.")
        return old_password

    def clean_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        if new_password:
            try:
                password_validation.validate_password(new_password, self.user)
            except ValidationError as e:
                raise forms.ValidationError(e)
        return new_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password and new_password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")
        return cleaned_data
