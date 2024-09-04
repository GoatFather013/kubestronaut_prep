# Use a lightweight base image
FROM alpine:latest

# Install necessary packages
RUN apk add --no-cache bash curl nmap

# Copy the script into the container
COPY spawn_processes.sh /usr/local/bin/spawn_processes.sh

# Make the script executable
RUN chmod +x /usr/local/bin/spawn_processes.sh

# Set the entrypoint to the script
ENTRYPOINT ["/usr/local/bin/spawn_processes.sh"]