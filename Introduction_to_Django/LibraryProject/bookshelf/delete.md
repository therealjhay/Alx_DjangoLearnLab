from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete() # This calls the delete() method on the book instance to remove it from the database
print(Book.objects.all())
