# advanced_features_and_security/users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Custom Admin interface for CustomUser model.
    Extends the default UserAdmin to display and edit custom fields.
    """
    model = CustomUser
    list_display = UserAdmin.list_display + ('date_of_birth', 'profile_photo',) # Add custom fields to list display
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
