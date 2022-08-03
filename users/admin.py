from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from users.models import Users_profile
# Register your models here.

User = get_user_model()

@admin.register(User)
# @admin.register(Users_profile)
class UserAdmin(UserAdmin):
    pass