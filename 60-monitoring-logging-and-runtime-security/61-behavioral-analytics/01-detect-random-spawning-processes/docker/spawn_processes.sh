#!/bin/bash

while true; do
  # Generate a random sleep interval between 1 and 10 seconds
  sleep_interval=$((RANDOM % 10 + 1))
  sleep $sleep_interval

  # Spawn a new process (e.g., a simple sleep command)
  commands=("curl" "ls -l" "nc -zv 8.8.8.8 53" "wget" "nmap")
  random_command=${commands[$RANDOM % ${#commands[@]}]}
  eval "$random_command" &
  echo "Spawned a new process with PID $!"
done