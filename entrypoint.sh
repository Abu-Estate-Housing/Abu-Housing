#!/usr/bin/env sh

echo "Applying migrations"
python manage.py migrate

exec "$@"
