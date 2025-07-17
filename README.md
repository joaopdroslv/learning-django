# Django Learning Project

This is my first Django project, built as a learning exercise to understand the basics of the Django framework. The project includes a simple employee listing and detail view system, demonstrating core features of Django such as URL routing, views, models, templates, and the ORM.

---

## 📚 Purpose

The main goal of this project was to get hands-on experience with:

- Django project/app structure
- Defining and registering URL routes
- Creating views to render templates
- Using Django’s ORM to interact with a database
- Building and extending HTML templates
- Managing static and media files

---

## 🔧 Features

- List of employees with basic information
- Employee detail page with more information
- Static homepage with a welcome message
- Base template extended by all pages
- Navigation between pages using URL routing

---

## ✅ Key Concepts Practiced

| Concept          | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **URL Routing**  | Defined in both the project (`mysite/urls.py`) and app level (`employees/urls.py`) |
| **Views**        | Function-based views created to handle requests and render templates         |
| **Templates**    | Used template inheritance with `base.html`, and created individual views     |
| **ORM**          | Created models in `models.py` and used Django ORM to interact with the database |
| **Admin Panel**  | Basic registration of the `Employee` model for admin access                  |

---

## 🚀 How to Run

1. Clone the repository
2. Navigate to the project folder
3. Create a virtual environment and install Django
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    pip install django
    ```
4. Run migrations and start the server
    ```bash
    cd src
    python manage.py migrate
    python manage.py runserver
    ```
5. Visit http://127.0.0.1:8000/ to view the homepage

---

📌 Notes
This project is intentionally simple and was developed for the purpose of understanding how Django works at a basic level. No authentication, advanced forms, or external integrations were added at this stage.
