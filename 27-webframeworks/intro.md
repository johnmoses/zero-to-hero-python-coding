# Web Frameworks

Web frameworks provide the tools and structure to build web applications and APIs in Python.

## Flask

Flask is a lightweight micro-framework — minimal by default, extensible as needed. Best for small apps and APIs.

```bash
pip install flask
```

```py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

- `app1/` — basic Flask app
- `app2/` — Flask with routes and templates

## Django

Django is a full-featured framework with batteries included — ORM, admin panel, authentication, and more. Best for large applications.

```bash
pip install django
django-admin startproject myproject
python manage.py runserver
```

Key components:
- **Models** — define database schema using Python classes
- **Views** — handle request logic
- **URLs** — map URLs to views
- **Admin** — auto-generated admin interface
- **Migrations** — version-controlled database changes

```py
# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
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
