#!/bin/bash
export SERVICE_IP=$(kubectl get svc -n imagepolicywebhook -o jsonpath='{.items[0].spec.clusterIP}')