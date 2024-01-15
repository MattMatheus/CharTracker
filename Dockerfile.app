# Dockerfile.app
# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install --no-cache-dir poetry
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copy project
COPY . /code/

# Run gunicorn
CMD ["poetry", "run", "gunicorn", "CharTracker.wsgi:application", "--bind", "0.0.0.0:8000"]