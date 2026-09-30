# Web: Scraping, Flask & Django

This chapter covers the full web stack — scraping data from the web, building lightweight apps with Flask, and full-featured applications with Django.

## Web Scraping

Web scraping extracts data from websites using `requests` and `beautifulsoup4`.

```bash
pip install requests beautifulsoup4
```

- `intro.py`, `scrape_i.py`, `scrape_ii.py` — scraping examples

## Flask

Flask is a lightweight micro-framework — minimal by default, extensible as needed.

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
