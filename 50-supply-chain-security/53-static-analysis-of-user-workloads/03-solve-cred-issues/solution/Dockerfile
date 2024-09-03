# Purposefully correct Dockerfile
FROM python:3.13.0rc1-alpine3.20

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Install packages
RUN pip install flask requests

# Copy application code
COPY . /app

# Set working directory
WORKDIR /app

# Change ownership of application files
RUN chown -R appuser:appgroup /app

# Expose port
EXPOSE 5000

# Define build argument for API key
ARG API_KEY

# Set environment variable using the build argument
ENV API_KEY=${API_KEY}

# Switch to the non-root user
USER appuser

# Run the application
CMD ["python", "app.py"]