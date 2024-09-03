# Purposefully incorrect Dockerfile

# Use an outdated base image
FROM python:2.7

# Run as root user
USER root

# Install packages without specifying versions
RUN pip install flask requests

# Copy application code
COPY . /app

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]