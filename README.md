# ALX Listing App (Deployed-ready)

A simple property/travel listings Django app ready for deployment with:
- Celery + RabbitMQ for background tasks
- Swagger UI at /swagger/
- Gunicorn + Procfile for WSGI
- docker-compose setup (Postgres + RabbitMQ + web + worker)

## Quick start (using Docker Compose)
1. Copy `.env.example` to `.env` and fill values.
2. Build and start services:
   ```bash
   docker-compose up --build -d
   ```
3. Run Django migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
   ```
4. Access the site: `http://localhost:8000/`
   - Swagger: `http://localhost:8000/swagger/`

## Without Docker (server deployment)
- Install dependencies from `requirements.txt`
- Configure env vars from `.env.example`
- Run migrations, start gunicorn, start celery worker pointing to the broker.

## Files included
- `alx_listing/` (Django project)
- `listings/` (Django app with models, serializers, views)
- `docker-compose.yml`, `Procfile`, `.env.example`
- `requirements.txt`
