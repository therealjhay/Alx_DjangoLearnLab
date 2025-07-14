from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete() # This method deletes the book instance from the database
print(Book.objects.all())
