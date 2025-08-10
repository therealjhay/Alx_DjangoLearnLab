# Advanced API Project

This project provides a RESTful API for managing a library of books.

## API Endpoints

### 📚 Books
- **GET /api/books/**: List all books.
  - **Permissions**: Read-only for unauthenticated users.
- **POST /api/books/create/**: Create a new book.
  - **Permissions**: Requires authentication.
- **GET /api/books/<id>/**: Retrieve a single book by ID.
  - **Permissions**: Read-only for unauthenticated users.
- **PUT /api/books/<id>/update/**: Update a book.
  - **Permissions**: Requires authentication.
- **DELETE /api/books/<id>/delete/**: Delete a book.
  - **Permissions**: Requires authentication.

## Custom View Configurations

The API uses Django REST Framework's **generic views** to simplify CRUD operations.
- `generics.ListAPIView` and `generics.RetrieveAPIView` are used for read-only access.
- `generics.CreateAPIView`, `generics.UpdateAPIView`, and `generics.DestroyAPIView` are used for creating, updating, and deleting resources, respectively.

### Permissions
- **`IsAuthenticatedOrReadOnly`** is applied to the list and detail views, allowing anyone to view the data but only authenticated users to modify it.
- **`IsAuthenticated`** is applied to the create, update, and delete views, ensuring that only logged-in users can perform these actions.