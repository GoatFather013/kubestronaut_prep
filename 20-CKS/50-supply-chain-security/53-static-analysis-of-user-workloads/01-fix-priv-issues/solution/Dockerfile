# Use a specific version of the base image
FROM ubuntu:24.04

# Run as root user
USER root

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Install packages
RUN apt-get update -y \
    && apt-get install -y vim curl wget python3 \
    && apt-get clean \
    && chown -R appuser:appgroup /app

# Copy application code
COPY . /app

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 8080

# Run as root user
USER appuser

# Run the application
CMD ["python3", "app.py"]