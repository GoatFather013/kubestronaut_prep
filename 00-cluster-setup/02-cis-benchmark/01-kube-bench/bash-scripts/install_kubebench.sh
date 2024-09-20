#!/bin/bash

# Download and install kube-bench
curl -L https://github.com/aquasecurity/kube-bench/releases/download/v0.8.0/kube-bench_0.8.0_linux_amd64.deb -o kube-bench_0.8.0_linux_amd64.deb
apt install ./kube-bench_0.8.0_linux_amd64.deb -f
apt install -y colorized-logs expect

# Create necessary directories
mkdir -p /opt/kube-bench/var/www/html/

# Create a script to publish the kube-bench results
cat << 'EOF' > /opt/kube-bench/pub_kubebench.sh
#!/bin/bash
unbuffer kube-bench | ansi2html > /opt/kube-bench/var/www/html/index.html
EOF

# Make the script executable
chmod +x /opt/kube-bench/pub_kubebench.sh

# Run the script
(crontab -l 2>/dev/null; echo "*/5 * * * * /opt/kube-bench/pub_kubebench.sh") | crontab -