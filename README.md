# Employee Registration System

A Django CRUD application for managing employee records. The app allows users to add, list, edit, and delete employees, while assigning each worker to a position such as Manager, Developer, or Accountant.

## Features

- Add new employee records
- View all employees in a table
- Update existing employee details
- Delete employee records
- Assign employees to a position
- Bootstrap 5 styling with crispy forms
- PostgreSQL database integration

## Tech Stack

- Python 3.10+
- Django 6.1.3
- PostgreSQL
- django-crispy-forms
- crispy-bootstrap5
- Pillow
- Bootstrap 5

## Project Structure

```text
djangoForms/
├── .venv/                   # Virtual environment
├── employeeProject/         # Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── employeeRegister/        # Main app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── static/                  # Static files
├── templates/               # HTML templates
│   ├── base.html
│   ├── employee_form.html
│   ├── employee_list.html
│   └── index.html
├── db.sqlite3               # Existing local database file
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Models

The application uses two main models:

- Position
  - Stores employee job titles
- Employee
  - Stores employee information such as full name, employee code, mobile number, and selected position

## Prerequisites

Before setting up the project, make sure you have:

- Python installed
- PostgreSQL installed and running
- A PostgreSQL database named `employees`
- Access to a local PostgreSQL user with privileges to create and manage tables

## Setup Instructions

1. Clone or open the project folder.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Make sure PostgreSQL is running and create the database:

```sql
CREATE DATABASE employees;
```

5. Update the database settings in `employeeProject/settings.py` if your local PostgreSQL credentials differ:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'employees',
        'USER': 'postgres',
        'PASSWORD': 'admin1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

6. Apply database migrations:

```bash
python manage.py migrate
```

7. Start the Django development server:

```bash
python manage.py runserver
```

8. Open the app in a browser:

```text
http://127.0.0.1:8000/
```

## Routes

- `/` - employee form page for creating or updating records
- `/list/` - employee list page
- `/<id>` - update page for a specific employee
- `/delete/<id>/` - delete an employee

## Notes

This project is intended for learning and local development. Before deployment, consider:

- moving secret configuration to environment variables
- setting `DEBUG = False` in production
- configuring `ALLOWED_HOSTS`
- using a secure production database setup
- adding authentication for admin access if needed

## Useful Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
