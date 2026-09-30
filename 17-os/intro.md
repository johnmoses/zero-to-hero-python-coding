# OS & Configuration

The `os` module provides functions for interacting with the operating system. Configuration covers reading environment variables and `.env` files to keep secrets out of source code.

## OS Module

Interact with the filesystem, directories, environment, and system time.

## Environment Variables & Config

Real applications never hardcode secrets. Environment variables keep config portable across dev, staging, and production.

```py
import os
db_url = os.environ.get("DATABASE_URL", "sqlite:///local.db")
```

Use `python-dotenv` to load a `.env` file at startup:

```bash
pip install python-dotenv
```

```py
from dotenv import load_dotenv
load_dotenv()
```

## Files

- `intro.py` — os module basics
- `cwd.py`, `listing.py`, `mkdir.py`, `rmdir.py` — filesystem operations
- `dir_exists.py` — checking paths
- `time.py` — system time
- `env_vars.py` — reading environment variables
- `dotenv_example.py` — loading .env with python-dotenv
- `.env.example` — template for required variables
