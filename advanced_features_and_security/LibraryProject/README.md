# Advanced Features and Security - Django Project

This project demonstrates custom user models, permissions, and groups in Django.

## Permissions and Groups Setup

This project implements a robust access control system using Django's built-in groups and custom permissions.

### 1. Custom Permissions (defined in `bookshelf/models.py`)

Custom permissions are defined on the `Book` model to allow granular control over book-related actions:
- `can_view`: Allows viewing book details and the book list.
- `can_create`: Allows adding new books.
- `can_edit`: Allows modifying existing books.
- `can_delete`: Allows removing books from the system.

These permissions are added to the `Book` model's `Meta` class:
```python
class Meta:
    permissions = [
        ("can_view", "Can view book"),
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]
