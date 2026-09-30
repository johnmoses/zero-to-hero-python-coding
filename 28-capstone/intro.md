# Capstone: Products REST API

A complete, production-style REST API that ties together everything in this course.

## What it covers

| Concept | Where used |
|---------|-----------|
| OOP + dataclasses | `models.py` — Product model |
| Exceptions + logging | `database.py` — error handling |
| Type hints | Throughout |
| FastAPI | `main.py` — routes |
| Environment variables | `config.py` — settings |
| Testing with pytest | `test_api.py` — full test suite |

## Project structure

```
30-capstone/
  main.py        — FastAPI app with CRUD routes
  models.py      — Product dataclass + in-memory store
  config.py      — settings from environment variables
  test_api.py    — pytest tests for all endpoints
```

## Run it

```bash
pip install fastapi uvicorn pytest httpx python-dotenv
uvicorn main:app --reload
```

API docs at: http://localhost:8000/docs

## Test it

```bash
pytest test_api.py -v
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /products | List all products |
| GET | /products/{id} | Get one product |
| POST | /products | Create a product |
| PUT | /products/{id} | Update a product |
| DELETE | /products/{id} | Delete a product |
