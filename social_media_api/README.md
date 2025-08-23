# Social Media API

This is a foundational social media API built with Django and Django REST Framework.

## Setup Instructions

1.  **Clone the repository.**
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You'll need to create a `requirements.txt` file by running `pip freeze > requirements.txt`)*
3.  **Run database migrations:**
    ```bash
    python manage.py makemigrations accounts
    python manage.py migrate
    ```
4.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### 1. User Registration

-   **URL:** `/api/accounts/register/`
-   **Method:** `POST`
-   **Body:** `{"username": "your_username", "email": "your_email@example.com", "password": "your_password"}`
-   **Response:** A JSON object containing a token and user details upon successful registration.

### 2. User Login

-   **URL:** `/api/accounts/login/`
-   **Method:** `POST`
-   **Body:** `{"username": "your_username", "password": "your_password"}`
-   **Response:** A JSON object containing a token for authentication.

## User Model Overview

The `CustomUser` model extends Django's `AbstractUser` and includes additional fields:
-   `bio`: A text field for a user's biography.
-   `profile_picture`: An image field to store the user's profile photo.
-   `followers`: A many-to-many relationship with itself to track who a user is following.