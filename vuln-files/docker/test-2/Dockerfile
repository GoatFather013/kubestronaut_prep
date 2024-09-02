# Purposefully incorrect Dockerfile

# Use a large base image with many vulnerabilities
FROM debian:latest

# Run as root user
USER root

# Install packages without specifying versions and without cleaning up
RUN apt-get update && apt-get install -y \
    netcat \
    telnet \
    ftp

# Copy application code
COPY . /app

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 80

# Run the application
CMD ["node", "server.js"]