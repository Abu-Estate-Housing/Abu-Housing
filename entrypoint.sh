#!/usr/bin/env sh

echo "Applying migrations"
python manage.py migrate
python manage.py collectstatic --no-input

exec "$@"
