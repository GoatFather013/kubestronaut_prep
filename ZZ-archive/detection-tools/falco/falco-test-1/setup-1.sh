#!/bin/bash

# Create a namespace for the exercise
kubectl create namespace falco-exercise1

# Deploy a pod with a vulnerable container
kubectl run vulnerable-pod --namespace=falco-exercise1 --image=alpine --command -- sleep 6000

echo "Setup complete. A pod 'vulnerable-pod' has been created in the 'falco-exercise1' namespace."