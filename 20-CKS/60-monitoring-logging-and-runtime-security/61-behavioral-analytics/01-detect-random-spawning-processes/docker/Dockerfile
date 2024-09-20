# Use a lightweight base image
FROM alpine:latest

USER root

# Install necessary packages
RUN apk add --no-cache bash curl nmap

# Create a non-root user and group
RUN addgroup -S mygroup && adduser -S myuser -G mygroup

# Copy the script into the container
COPY spawn_processes.sh /usr/local/bin/spawn_processes.sh

# Make the script executable
RUN chmod +x /usr/local/bin/spawn_processes.sh

# Change ownership of the script to the non-root user
RUN chown myuser:mygroup /usr/local/bin/spawn_processes.sh

# Switch to the non-root user
USER myuser

# Set the entrypoint to the script
ENTRYPOINT ["/usr/local/bin/spawn_processes.sh"]