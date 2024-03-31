from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUsersAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        *UserAdmin.fieldsets,
        ("Кастомные надстройки", {"fields": ("web_points", "reverse_points", "other_points", "osint_points",
                                             "crypto_points", "birth_date", 'user_data')}),
    )
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (None, {"fields": ("birth_date", )}),
    )
