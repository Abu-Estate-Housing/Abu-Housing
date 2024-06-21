FROM python:3.11.4-alpine

WORKDIR /app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

Run pip install --upgrade pip

Copy ./requirements.txt /app
Run pip install -r requirements.txt

Copy ./entrypoint.sh /entrypoint.sh
Run chmod +x /entrypoint.sh
Copy . /app

ENTRYPOINT ["/entrypoint.sh"]
