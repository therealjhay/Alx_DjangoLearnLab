# bookshelf/admin.py

from django.contrib import admin
from .models import Book

# Register your models here.

# Customize the Django admin interface for the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the display and functionality of the Book model
    in the Django administration interface.
    """
    # list_display: Controls which fields are displayed on the change list page of the admin.
    # This makes it easy to see key information about each book at a glance.
    list_display = ('title', 'author', 'publication_year')

    # list_filter: Adds filters to the right sidebar of the change list page,
    # allowing users to quickly narrow down the list of books.
    # Here, we can filter by publication_year and author.
    list_filter = ('publication_year', 'author')

    # search_fields: Enables a search box on the change list page.
    # Django will search for text in the specified fields.
    # This allows administrators to find books by title or author.
    search_fields = ('title', 'author')

    # list_per_page: Sets the number of items to display per page in the change list.
    list_per_page = 25

    # ordering: Defines the default ordering for the list of books.
    # Books will be ordered by title alphabetically.
    ordering = ('title',)

    ["admin.site.register(CustomUser, CustomUserAdmin)"]

    # fields: Controls the order of fields on the edit form.
    # If not specified, fields will appear in the order they are defined in the model.
    # fields = ('title', 'author', 'publication_year') # Optional: uncomment to explicitly order fields on the edit form

    # readonly_fields: Makes specified fields read-only in the admin form.
    # For example, if you wanted the publication_year to be uneditable after creation:
    # readonly_fields = ('publication_year',)
