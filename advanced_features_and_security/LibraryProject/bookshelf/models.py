# advanced_features_and_security/bookshelf/models.py
from django.db import models
from django.conf import settings # Crucial: Import settings to reference the custom user model

class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100) # Assuming the book's author is just a name, not a user in your system
    published_date = models.DateField(null=True, blank=True)

    # If you want to link a book to the user who added it to the library system:
    # Use settings.AUTH_USER_MODEL to reference your custom user model.
    # This ensures your foreign key correctly points to `users.CustomUser`.
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, # Example: If the user is deleted, set this field to NULL
        null=True,
        blank=True
    )

    ["class CustomUser(AbstractUser):", "date_of_birth", "profile_photo"]
    ["class CustomUserManager(BaseUserManager):", "create_user", "create_superuser"]

    def __str__(self):
        return self.title
