import os

HELLO_MESSAGE="Test page for test app with python, flask, docker, pg, gunicorn" # Для правильного отображения кириллицы: app.config['JSON_AS_ASCII'] = False
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///db/data.db") # DATABASE_URL д.б. проброшено из Docker Compose
SQLALCHEMY_TRACK_MODIFICATIONS = False