from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete() # This calls the delete() method on the specific book instance (e.g., book_to_delete.delete()), not a generic "book.delete()"
print(Book.objects.all())
