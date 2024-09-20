#!/bin/bash

# Check if Falco detected suspicious shell activity
grep "Terminal shell in container" /var/log/falco.log | grep "vulnerable-pod"
if [ $? -eq 0 ]; then
    echo "Validation passed: Suspicious shell activity detected in the 'vulnerable-pod' container."
else
    echo "Validation failed: No suspicious shell activity detected."
    exit 1
fi