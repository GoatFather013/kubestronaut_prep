#!/bin/bash
curl -L https://github.com/aquasecurity/kube-bench/releases/download/v0.8.0/kube-bench_0.8.0_linux_amd64.deb -o kube-bench_0.8.0_linux_amd64.deb
apt install ./kube-bench_0.8.0_linux_amd64.deb -f
apt install -y colorized-logs expect
mkdir -p /opt/kube-bench/var/www/html/