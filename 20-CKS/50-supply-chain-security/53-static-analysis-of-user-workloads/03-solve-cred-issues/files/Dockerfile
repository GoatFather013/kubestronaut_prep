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

# Hardcode sensitive information (credential issue)
ENV API_KEY="12345-abcde-67890-fghij"

# Run as root user
USER root

# Run the application
CMD ["python", "app.py"]