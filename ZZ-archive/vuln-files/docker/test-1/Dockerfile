# Purposefully incorrect Dockerfile

# Use a large base image with many vulnerabilities
FROM ubuntu:latest

# Run as root user
USER root

# Install packages without specifying versions
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    vim

# Copy application code
COPY . /app

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 8080

# Run the application
CMD ["python3", "app.py"]