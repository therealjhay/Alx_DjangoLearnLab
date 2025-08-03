from bookshelf.models import Book
book_1984 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book_1984)
