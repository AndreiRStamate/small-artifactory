#!/bin/bash

echo "Killing ngrok and Flask..."
pkill -f ngrok
pkill -f app.py
echo "✅ Stopped."