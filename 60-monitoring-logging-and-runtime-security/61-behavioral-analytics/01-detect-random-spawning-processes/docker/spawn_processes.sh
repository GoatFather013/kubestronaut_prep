#!/bin/bash

LOG_FILE="/var/log/spawn_processes.log"

while true; do
  # Generate a random sleep interval between 1 and 10 seconds
  sleep_interval=$((RANDOM % 10 + 1))
  sleep $sleep_interval

  # Spawn a new process (e.g., a simple sleep command)
  commands=(
    "nc -l -p 1234 || true"  # Listening on a network port
    "sh -c 'echo Hello' || true"  # Shell spawning from a non-shell parent
    "ls / || true"  # Listing root directory
    "cat /proc/cpuinfo || true"  # Reading CPU info
    "chmod 777 /tmp || true"  # Modifying permissions of a temporary directory
  )
  random_command=${commands[$RANDOM % ${#commands[@]}]}
  eval "$random_command" >> "$LOG_FILE" 2>&1 &
  echo "Spawned a new process with PID $!" >> "$LOG_FILE" 2>&1
done