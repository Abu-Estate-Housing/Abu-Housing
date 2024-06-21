#!/usr/bin/env sh

echo "Installing requirements file"
pip install -r requirements.txt
echo "Applying migrations"
python manage.py migrate

exec "$@"
