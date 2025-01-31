# Use a lightweight base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    jpeg-dev \
    zlib-dev \
    postgresql-dev


# Set the working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code
COPY . .

# Collect static files during build time (optional)
RUN python manage.py collectstatic --noinput

# Expose the desired port
EXPOSE 8000

# Default command to run the Django app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application", "--access-logfile", "-", "--workers=3"]
