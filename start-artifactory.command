#!/bin/bash

# Navigate to the project directory (change this to your actual path)
cd "$(dirname "$0")"

# Start the server
nohup python3 run_server.py &
echo "Server started! Check server.log for output."