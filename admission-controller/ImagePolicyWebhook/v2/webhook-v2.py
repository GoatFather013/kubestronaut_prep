#!/bin/env python3

# A simple imagePolicyWebhook admission controller that allows images based on a wildcard pattern
# and disallows specific images in the cluster, with exemptions for certain namespaces.
# Only to play with the imagePolicyWebhoook for the CKS certification
# Not useful, not secure and not for production.

# Import modules
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
from io import BytesIO
import json
import fnmatch
from kubernetes import client, config

# Load Kubernetes configuration
config.load_incluster_config()

# Read the ConfigMap
v1 = client.CoreV1Api()
config_map_allow = v1.read_namespaced_config_map("webhook-config-allow", "imagepolicywebhook")
config_map_disallow = v1.read_namespaced_config_map("webhook-config-disallow", "imagepolicywebhook")
config_map_exempt = v1.read_namespaced_config_map("webhook-config-exempt", "imagepolicywebhook")

# Define the allowed wildcard pattern and disallowed images
# ALLOWED_PATTERN = ["nginx*", "alpine*", "busybox*", "ubuntu*", "redis*", "mysql*"
# DISALLOWED_IMAGES = ["*:latest"]
# EXEMPTED_NAMESPACES = ["kube-system", "imagepolicywebhook"]

ALLOWED_PATTERN = config_map_allow.data['allowed_patterns'].split(',')
DISALLOWED_IMAGES = config_map_disallow.data['disallowed_images'].split(',')
EXEMPTED_NAMESPACES = config_map_exempt.data['exempted_namespaces'].split(',')

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

        # Extract the namespace and image name from the request
        namespace = request['request']['object']['metadata']['namespace']
        image = request['request']['object']['spec']['containers'][0]['image']

        # Check if the namespace is exempted
        if namespace in EXEMPTED_NAMESPACES:
            # Allow the request
            response = {
                "response": {
                    "allowed": True
                }
            }
        # Check if the image is disallowed
        elif image in DISALLOWED_IMAGES:
            # Deny the request
            response = {
                "response": {
                    "allowed": False,
                    "status": {
                        "message": f"Image '{image}' is disallowed"
                    }
                }
            }
        # Check if the image matches the allowed pattern
        elif any(fnmatch.fnmatch(image, pattern) for pattern in ALLOWED_PATTERN):
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
                        "message": f"Image '{image}' does not match the allowed pattern '{ALLOWED_PATTERN}'"
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