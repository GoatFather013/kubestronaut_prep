# Use a smaller base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the webhook script
COPY ./webhook-v2.py .

# Set the entrypoint
ENTRYPOINT ["python", "./webhook-v2.py"]