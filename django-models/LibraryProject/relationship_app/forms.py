# relationship_app/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    Form for creating and updating Book instances.
    """
    class Meta:
        model = Book
        fields = ['title', 'author'] # Fields that can be edited via the form
