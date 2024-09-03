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
import os
from kubernetes import client, config

# Load environment variables
ALLOWED_PATTERN = os.getenv('allowed_patterns', '').split(',')
DISALLOWED_IMAGES = os.getenv('disallowed_images', '').split(',')
EXEMPTED_NAMESPACES = os.getenv('exempted_namespaces', '').split(',')

# Print a message to indicate the server is starting
print("Starting webhook")

# Define a custom request handler by inheriting from BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Set the HTTP protocol version
    protocol_version = "HTTP/1.1"

    # Respond to a GET request
    def do_GET(self):
        self.send_response(200)  # Set the response status code
        self.end_headers()  # Send an empty line to indicate the end of the headers
        self.wfile.write(  # Send a response body
            b"I am a imagePolicyWebhook example!\nYou need to post a json object of kind ImageReview"
        )

    def do_POST(self):
        # # Print environment variables for debugging
        # print("Allowed patterns:", os.getenv('allowed_patterns'))
        # print("Disallowed images:", os.getenv('disallowed_images'))
        # print("Exempted namespaces:", os.getenv('exempted_namespaces'))

        # Read the length of the request body
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Decode the byte string to a regular string
        post_data_str = post_data.decode('utf-8')

        # Parse the JSON string to a Python dictionary
        request = json.loads(post_data_str)

        # Check if the request is an ImageReview
        if request['kind'] != 'ImageReview':
            print("Invalid request kind")
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Bad Request')
            return
        
        # Log the incoming request for debugging
        print("Incoming request:", json.dumps(request, indent=4))

        # Check if the request includes annotations
        annotations = request['spec'].get('annotations')
        if annotations:
            print("Annotations:", annotations)
        
        # Check if the request includes a namespace
        namespace = request['spec'].get('namespace')
        if namespace:
            print("Namespace:", namespace)

        # Check if the request includes images
        images = request['spec'].get('containers')
        if images:
            print("Images:", images)
        
        if namespace in EXEMPTED_NAMESPACES:
            print("namespace statement works")
            request["status"] = {
                "allowed": True,
                "reason": "Namespace does not have restrictions"
            }

        # try:
        #    # Extract the namespace and image name from the request
        #    namespace = request['spec']['namespace']
        #    image = request['spec']['containers'][0]['image']
        #    print(f"Namespace: {namespace}, Image: {image}")
        # except KeyError as e:
        #    print(f"KeyError: {e}")
        #    self.send_response(400)
        #    self.end_headers()
        #    self.wfile.write(b'Bad Request')
        #    return

        # # Log the exempted namespaces for debugging
        # print("Exempted namespaces:", EXEMPTED_NAMESPACES)

        # # Check if the namespace is exempted
        # if namespace in EXEMPTED_NAMESPACES:
        #     print(f"Namespace '{namespace}' is exempted.")
        #     # Allow the request
        #     response = {
        #         "response": {
        #             "allowed": True
        #         }
        #     }
        # else:
        #     # Log the allowed patterns and disallowed images for debugging
        #     print("Allowed patterns:", ALLOWED_PATTERN)
        #     print("Disallowed images:", DISALLOWED_IMAGES)

        #     # Check if the image is disallowed
        #     if any(fnmatch.fnmatch(image, pattern) for pattern in DISALLOWED_IMAGES):
        #         print(f"Image '{image}' is disallowed.")
        #         # Deny the request
        #         response = {
        #             "response": {
        #                 "allowed": False,
        #                 "status": {
        #                     "message": f"Image '{image}' is disallowed"
        #                 }
        #             }
        #         }
        #     else:
        #         # Allow the request
        #         response = {
        #             "response": {
        #                 "allowed": True
        #             }
        #         }

        # Write the response
        response_body = json.dumps(request)  
        # Convert the response body from JSON to bytes

        # Log the response being sent back
        print("Sending response:", response_body)

        # Send the response back to the client
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(response_body.encode('utf-8'))

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