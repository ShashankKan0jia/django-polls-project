# Django Polls Project

A Django learning project centered around a polls application.

## Structure
- `manage.py` — Django command-line entry point
- `mysite/` — project configuration
- `polls/` — polls application
- `db.sqlite3` — current local SQLite database

## Run locally
`python manage.py migrate`
`python manage.py runserver`

For deployment, separate secrets, database configuration, static files, and environment-specific settings from source control.