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

CMD ["./initial_script.sh"]
