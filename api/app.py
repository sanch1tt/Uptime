from flask import Flask, send_from_directory
import threading
import time
import requests
import os

app = Flask(__name__)

# 🔁 Set your target URL here
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
    return '''
        <html>
            <head>
                <title>Uptime Pinger</title>
                <link rel="icon" href="/favicon.ico" type="image/x-icon">
            </head>
            <body>
                <h1>Uptime Pinger is Running! 🚀</h1>
            </body>
        </html>
    '''

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

# Start background thread
def start_background_pinger():
    thread = threading.Thread(target=ping_target, daemon=True)
    thread.start()

if __name__ == '__main__':
    start_background_pinger()
    app.run(host='0.0.0.0', port=7860)
