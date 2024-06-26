from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, OtpCode
from .forms import UserChangeForm, UserCreationForm

# Register your models here.


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "code", "created")


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ["email", "is_admin", "phone_number"]
    list_filter = ["is_admin", "is_superuser"]
    readonly_fields = ("last_login",)
    fieldsets = [
        ("Main", {"fields": ("email", "phone_number", "full_name", "password")}),
        (
            "Permission",
            {
                "fields": (
                    "is_admin",
                    "is_active",
                    "last_login",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    ]

    add_fieldsets = [
        (
            None,
            {
                "fields": (
                    "email",
                    "phone_number",
                    "full_name",
                    "password1",
                    "password2",
                )
            },
        ),
    ]

    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = [
        "groups",
        "user_permissions",
    ]


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
