# APIs and FastAPI

## What is an API

Application Programming Interface (API) is a medium through which applications expose their functionality to other systems. Interactions between provider and consumer are regulated by a contract (endpoints, request/response format, auth).

## REST

Representational State Transfer (REST) is an architectural style for APIs over HTTP. It uses standard HTTP methods:

| Method | Action |
|--------|--------|
| GET | Read |
| POST | Create |
| PUT | Update (full) |
| PATCH | Update (partial) |
| DELETE | Remove |

## FastAPI

FastAPI is a modern, high-performance async web framework for building APIs with Python. It uses type hints to auto-generate validation and documentation.

```bash
pip install fastapi uvicorn
```

```py
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Hello, World!'}

@app.get('/users/{user_id}')
def get_user(user_id: int):
    return {'user_id': user_id}
```

Run with:

```bash
uvicorn main:app --reload
```

Auto-generated docs available at `http://localhost:8000/docs`

## FastAPI vs Flask vs Django REST

| | FastAPI | Flask | Django REST |
|---|---|---|---|
| Performance | Highest (async) | Medium | Medium |
| Auto docs | Yes (OpenAPI) | No | Partial |
| Validation | Built-in (Pydantic) | Manual | Serializers |
| Best for | High-performance APIs | Simple APIs | Django projects |

- `app1/` — basic FastAPI app
- `app2/` — FastAPI with HTML + endpoints
- `app_i.py` to `app_iv.py` — REST API examples with Flask and MongoDB
