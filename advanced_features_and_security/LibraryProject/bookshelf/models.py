# advanced_features_and_security/bookshelf/models.py
from django.db import models
from django.conf import settings # Import settings to reference AUTH_USER_MODEL

class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100) # Assuming book author is not necessarily a user
    published_date = models.DateField(null=True, blank=True)
    # If a book is "uploaded" or "added" by a user:
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, # Always use settings.AUTH_USER_MODEL for FKs to User
        on_delete=models.SET_NULL, # Or models.CASCADE, models.PROTECT, etc., based on your logic
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

# If you had a 'UserProfile' model before, you might merge its fields into CustomUser
# or keep it if it holds data specific to an app rather than the core user.
# For this task, we assume the new fields are enough.
