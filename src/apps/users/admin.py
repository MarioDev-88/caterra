from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import User, Admin, Seller, Editor, Customer
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ("first_name", "first_surname", "email", "is_superuser")
    list_filter = ("is_superuser",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "first_surname", "phone")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide"),
                "fields": (
                    "first_name",
                    "first_surname",
                    "last_surname",
                    "email",
                    "phone",
                    "password",
                    "password2",
                ),
            },
        ),
        ("permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    search_fields = (
        "email",
        "first_name",
        "first_username",
        "last_surname",
    )

    ordering = ("email",)

    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(Admin)
admin.site.register(Seller)
admin.site.register(Editor)
admin.site.register(Customer)
