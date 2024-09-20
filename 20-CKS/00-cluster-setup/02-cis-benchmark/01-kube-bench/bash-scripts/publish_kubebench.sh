#!/bin/bash
unbuffer kube-bench | ansi2html > /opt/kube-bench/var/www/html/index.html