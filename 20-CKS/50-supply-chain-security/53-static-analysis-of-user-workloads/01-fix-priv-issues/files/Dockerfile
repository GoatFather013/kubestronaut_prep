# Purposefully incorrect Dockerfile
# Use a large base image with many vulnerabilities
FROM ubuntu:latest

# Run as root user
USER root

# Install packages && creating caching layers
RUN apt-get update -y vim
RUN apt-get install -y
RUN apt-get install -y curl
RUN apt-get install -y wget

# Copy application code
COPY . /app

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 8080

USER ROOT

# Run the application
CMD ["python3", "app.py"]