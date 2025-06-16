from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

# 🔁 Set your target Render URL here
TARGET_URL = "https://direct-download.onrender.com/"

# 🔄 Background task to ping every 60 seconds
def ping_target():
    while True:
        try:
            response = requests.get(TARGET_URL)
            print(f"[{time.ctime()}] Pinged {TARGET_URL} - Status: {response.status_code}", flush=True)
        except Exception as e:
            print(f"[{time.ctime()}] Ping failed: {e}", flush=True)
        time.sleep(60)

@app.route('/')
def home():
    return "Uptime Pinger is Running!", 200

# Start pinging as a background thread
def start_background_pinger():
    thread = threading.Thread(target=ping_target, daemon=True)
    thread.start()

if __name__ == '__main__':
    start_background_pinger()
    app.run(host='0.0.0.0', port=7860)
