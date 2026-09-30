# Web Frameworks: Flask & Django

Web frameworks provide the tools and structure to build web applications in Python.

## Flask

Flask is a lightweight micro-framework — minimal by default, extensible as needed. Best for small apps and APIs.

```bash
pip install flask
```

- `app1/` — basic Flask app
- `app2/` — Flask with routes and templates

## Django

Django is a full-featured framework with batteries included — ORM, admin panel, authentication, migrations.

```bash
pip install django
django-admin startproject myproject
python manage.py runserver
```

- `django-app1/` — Django project with users app
- `django-app2/` — Django project with books and users apps

## Flask vs Django

| | Flask | Django |
|---|---|---|
| Size | Micro | Full-stack |
| Flexibility | High | Opinionated |
| ORM | External (SQLAlchemy) | Built-in |
| Best for | APIs, small apps | Large web apps |
