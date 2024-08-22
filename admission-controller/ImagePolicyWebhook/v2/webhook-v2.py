#!/bin/env python3

# A simple imagePolicyWebhook admission controller that only allows nginx images with a specific tag in the cluster
# Only to play with the imagePolicyWebhoook for the CKS certification
# Not useful, not secure and not for production.

# Import modules
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
from io import BytesIO
import json

# Set the allowed image name and tag
ALLOWED_IMAGE = "nginx"
ALLOWED_TAG = "1.19.6"

# Print a message to indicate the server is starting
print("Starting webhook")

# Define a custom request handler by inheriting from BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Set the HTTP protocol version
    protocol_version = "HTTP/1.1"

    def do_POST(self):
        # Read the length of the request body
        content_length = int(self.headers['Content-Length'])
        # Read the request body
        body = self.rfile.read(content_length)
        # Parse the request body as JSON
        request = json.loads(body)

        # Extract the image name and tag from the request
        image = request['request']['object']['spec']['containers'][0]['image']
        image_name, image_tag = image.split(":")

        # Check if the image name and tag match the allowed values
        if image_name == ALLOWED_IMAGE and image_tag == ALLOWED_TAG:
            # Allow the request
            response = {
                "response": {
                    "allowed": True
                }
            }
        else:
            # Deny the request
            response = {
                "response": {
                    "allowed": False,
                    "status": {
                        "message": f"Only {ALLOWED_IMAGE}:{ALLOWED_TAG} images are allowed"
                    }
                }
            }

        # Write the response
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

# Create an HTTP server on port 443 with an SSL context and certificate/key files
httpd = HTTPServer(("0.0.0.0", 443), SimpleHTTPRequestHandler)
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(
    certfile="/etc/ssl/certs/webhook-server.crt",
    keyfile="/etc/ssl/private/webhook-server.key",
)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

# Start the Webhook
httpd.serve_forever()