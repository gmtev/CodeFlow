from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from CodeFlow.accounts.forms import CustomUserCreationForm, CustomUserChangeForm

UserModel = get_user_model()


@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    model = UserModel
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ('pk', 'email', 'username', 'is_staff', 'is_superuser', )
    search_fields = ('email',)
    ordering = ('pk',)
    list_filter = ('is_staff', 'is_superuser', 'username')
    readonly_fields = ('pk', )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )