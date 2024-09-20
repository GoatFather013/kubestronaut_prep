# Use a minimal base image
FROM node:alpine

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set the working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install necessary packages and clean up
RUN apk add --no-cache \
    netcat-openbsd \
    busybox-extras \
    && chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

# Expose port
EXPOSE 80

# Run the application
CMD ["node", "server.js"]