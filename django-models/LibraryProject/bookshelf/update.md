from bookshelf.models import Book
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save() # Save the changes to the database
print(f"Updated Title: {book_to_update.title}") # Note: We use 'book_to_update.title' here, not 'book.title'
