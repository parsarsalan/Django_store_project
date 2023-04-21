from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUserModel
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('username', 'email',)


