import subprocess
import time
import requests
import webbrowser
import os
import sys
# Open log file and redirect all output to it
log_file = open("server.log", "a")
sys.stdout = log_file
sys.stderr = log_file

# STEP 1: Start Flask in the background
flask_process = subprocess.Popen(
    ["python3", "/Users/a144185i/workspace/small-artifactory/app.py"],
    stdout=log_file,
    stderr=log_file
)
print("✅ Flask server started on http://localhost:6969")

# STEP 2: Start ngrok in the background
ngrok_process = subprocess.Popen(
    ["ngrok", "http", "6969"],
    stdout=log_file,
    stderr=log_file
)
print("🌐 Starting ngrok tunnel...")

# STEP 3: Wait a few seconds for ngrok to fully start
time.sleep(2)

# STEP 4: Get the public URL from ngrok's local API
try:
    tunnel_info = requests.get("http://localhost:4040/api/tunnels").json()
    public_url = tunnel_info['tunnels'][0]['public_url']
    print(f"🚀 Public URL: {public_url}")
    # Optionally open the URL in a browser
    webbrowser.open(public_url + "/files")
except Exception as e:
    print("⚠️ Could not get ngrok URL:", e)

print("📡 Flask + ngrok are running. Press CTRL+C to stop.")

# STEP 5: Wait for Flask process to finish
try:
    flask_process.wait()
except KeyboardInterrupt:
    print("🛑 Stopping servers...")
    flask_process.terminate()
    ngrok_process.terminate()

# Close log file on exit
log_file.close()
