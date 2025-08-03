from bookshelf.models import Book
retrieved_book = Book.objects.get(title="1984")
print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Publication Year: {retrieved_book.publication_year}")
