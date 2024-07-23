# celery docker

```docker
# FROM python:3.7.3-slim
FROM python:3.8.16
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any necessary dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
CMD celery -A run_celery.celery worker --loglevel=info --concurrency=2
#CMD celery -A run_celery.celery worker --loglevel=info -B
```
# celery beat
```docker
# FROM python:3.7.3-slim
FROM python:3.8.16
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any necessary dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
# Start the Celery workers
# CMD celery -A run_celery.celery worker --loglevel=info -B
CMD celery -A run_celery.celery beat --loglevel=info
```
