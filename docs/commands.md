# 📘 Django – Basic Commands

This guide covers the most commonly used Django CLI commands for project and app management.

---

## 🚀 Start a new Django project

```bash
django-admin startproject <project_name> .
```
Initializes a new Django project in the current directory.

## 🧱 Create a new app

```bash
python manage.py startapp <app_name>
```
Creates a new Django app inside your project.

## 🔧 Apply migrations (create/update database tables)

```bash
python manage.py makemigrations
python manage.py migrate
```
makemigrations: Creates new migration files based on model changes.
migrate: Applies those migrations to the database.

## 👤 Create a superuser

```bash
python manage.py createsuperuser
```
Creates an admin user for accessing the Django admin panel.

## 🔑 Change user password

```bash
python manage.py changepassword <username>
```
Changes the password for an existing user.

## ▶️ Run the development server

```bash
python manage.py runserver
```
Starts the local development server at http://127.0.0.1:8000/.

## 📄 Show all available commands

```bash
python manage.py help
```
Lists all available management commands.

## 🧪 Run tests

```bash
python manage.py test
```
Runs the tests for your Django apps.

## 📂 Show SQL for a migration

```bash
python manage.py sqlmigrate <app_name> <migration_number>
```
Outputs the SQL statements for a specific migration (e.g., 0001).

## 📜 Show all models in the project

```bash
python manage.py showmigrations
```
Displays all migrations and their status (applied or not).

## 🧹 Clear all .pyc files

```bash
python manage.py clean_pyc
```
If you’ve installed django-extensions, this clears compiled Python files.

## 🔄 Create a custom command

To create a custom management command:

1. Inside your app, create the folder: `management/commands/`
2. Add an `__init__.py` in both folders.
3. Create a command file (e.g., `hello.py`) with a `Command` class inheriting from `BaseCommand`.