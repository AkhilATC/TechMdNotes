# Flask - celery
```python
# factory.py
from flask import Flask
from celery import Celery
from config import Config
from flask_pymongo import PyMongo
from flask_mail import Mail
import os
import celeryconfig
from flask_opensearch import FlaskOpenSearch


app = Flask(__name__)
celery = Celery(__name__)
# mongo = PyMongo()
# mail = Mail()
# opensearch = FlaskOpenSearch()


def make_app():
    env = os.environ.get("ENVIRONMENT", "local")
    app.config.from_object(Config(env=env))
    celery.conf.update(app.config)
    celery.config_from_object(celeryconfig)
    # mongo instance init
    # mongo.init_app(app)
    # opensearch instance init
    # opensearch.init_app(app)
    # mail service init
    # mail.init_app(app)
    # controller import and register blueprints
    # app.register_blueprint(log_reasoner_interface)
    return app


def make_celery(app):
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

```
# celery - beat worker config
```python
# celeryconfig
from celery.schedules import crontab

CELERY_IMPORTS = ('src.tasks.schedule_tasks')
CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'test-celery': {
        'task': 'src.tasks.scheduled_tasks',
        # Every minute
        'schedule': crontab(minute="*"),
    }
}
```
## run and run celery
```python3
# run.py
from factory import make_app  # make_celery

app = make_app()
app.run(host="0.0.0.0", port=5500, debug=True)
# celery = make_celery(app)
# run_celery
from factory import make_app, make_celery
import redis
import os

app = make_app()
app.app_context().push()
app.config["REDIS_PASSWORD"] = os.environ.get('REDIS_PASSWORD')
celery = make_celery(app)

```
# Dockerfile
- app
```dockerfile
#FROM python:3.7.3-slim
FROM python:3.8.16
# We copy just the requirements.txt first to leverage Docker cache
WORKDIR /apps
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip3 --no-cache-dir install -r requirements.txt
COPY . /apps
ENTRYPOINT [ "python3", "./run.py" ]
# CMD ["gunicorn", "--bind", "0.0.0.0:5500", "--workers=4", "--timeout=999", "run:app"]
```
- worker
```dockerfile
# Use a Python runtime as a parent image
# FROM python:3.7.3-slim
FROM python:3.8.16

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Start the Celery worker
CMD celery -A run_celery.celery worker --loglevel=info --concurrency=2

```
- beat-worker
```dockerfile
# FROM python:3.7.3-slim
FROM python:3.8.16

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Start the Celery worker
# CMD celery -A run_celery.celery worker --loglevel=info -B
CMD celery -A run_celery.celery beat --loglevel=info

```

