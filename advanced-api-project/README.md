# Book API — Views & Endpoints

## Public Endpoints
- `GET /api/books/` → List all books
- `GET /api/books/<id>/` → Retrieve a single book

## Authenticated Endpoints
- `POST /api/books/create/` → Create new book
- `PUT /api/books/<id>/update/` → Update a book
- `DELETE /api/books/<id>/delete/` → Delete a book

### Permissions:
- Read: Anyone
- Write: Authenticated users only

### Custom Validations:
- `publication_year` cannot be in the future (enforced in Create & Update views).
