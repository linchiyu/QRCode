# Django QR Code Project

## Overview
A Django 5.x project scaffold to build QR code-related features. This README guides you through local setup, development, and deployment.

## Tech Stack
- **Python**: 3.10+ recommended
- **Django**: 5.x
- **Database**: SQLite (dev)
- **OS**: macOS (commands below), works on Linux/Windows with minor changes

## Prerequisites
- Python 3 installed: `python3 --version`
- Git (optional but recommended)

## Quick Start

### 1) Open the project root
```bash
cd /Users/linchiyu/Documents/QRCode
```

### 2) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Upgrade packaging tools
```bash
python -m pip install --upgrade pip setuptools wheel
```

### 4) Install dependencies
If `requirements.txt` exists:
```bash
pip install -r requirements.txt
```
If not yet created:
```bash
pip install "Django>=5,<6"
pip freeze > requirements.txt
```

### 5) Create Django project and app (if not already created)
From the project root:
```bash
django-admin startproject qrcode_site .
python manage.py startapp qr
```

### 6) Configure settings
Edit `qrcode_site/settings.py`:
- Add `'qr'` to `INSTALLED_APPS`.
- Set time zone and allowed hosts:
```python
TIME_ZONE = "America/Sao_Paulo"
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```

Optional environment variables support:
- Create `.env` in the project root (if you plan to use one).
- Never commit real secrets; add `.env` to `.gitignore`.

### 7) Apply migrations and run server
```bash
python manage.py migrate
python manage.py runserver
```
Visit http://127.0.0.1:8000/

## Project Structure
After initialization, you’ll have something like:
```
QRCode/
├─ .venv/
├─ qrcode_site/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ qr/
│  ├─ migrations/
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ tests.py
│  └─ views.py
├─ manage.py
├─ requirements.txt
└─ README.md
```

## Environment Configuration
- Create `.env` (optional) to store secrets:
```
DEBUG=True
SECRET_KEY=change-me
DATABASE_URL=sqlite:///db.sqlite3
```
- If you use `django-environ` or similar, wire it in `settings.py` accordingly.

## Common Commands
- Start server: `python manage.py runserver`
- Make migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`
- Open shell: `python manage.py shell`
- Collect static (for production): `python manage.py collectstatic`

## Testing
- Run tests:
```bash
python manage.py test
```
- Add tests in `qr/tests.py`.

## Code Style (optional but recommended)
- Install tools:
```bash
pip install black isort flake8
```
- Format:
```bash
black .
isort .
```
- Lint:
```bash
flake8
```

## Git Ignore
Create `.gitignore`:
```
.venv/
__pycache__/
*.pyc
db.sqlite3
*.log
.env
staticfiles/
```

## Deployment (Brief)
- Set `DEBUG=False` in production.
- Set `ALLOWED_HOSTS` to your domain(s).
- Use Gunicorn + Nginx (example):
```bash
pip install gunicorn
gunicorn qrcode_site.wsgi:application --bind 0.0.0.0:8000
```
- Run `collectstatic` and serve static files with the web server.
- Configure a production database (e.g., Postgres) and `SECRET_KEY` via environment variables.

## Troubleshooting
- Command not found: Activate venv: `source .venv/bin/activate`
- Port in use: Change runserver port: `python manage.py runserver 8001`
- Migration issues: `rm db.sqlite3` and `rm -rf qr/migrations` (except `__init__.py`) only if safe, then re-run migrations.
- Permission issues on macOS: Try `python -m pip ...` instead of `pip ...` to use venv’s interpreter.

## Contributing
- Fork, create a feature branch, commit with clear messages, open a PR.
- Include tests for new behavior.

## License
Choose a license (MIT/BSD/Apache-2.0). Add a `LICENSE` file.
