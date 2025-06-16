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
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Uptime Pinger</title>
        <link rel="icon" href="/favicon.ico" type="image/x-icon">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #0f1f2d;
                color: #fff;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                padding-bottom: 60px;
            }

            .container {
                background: rgba(255, 255, 255, 0.05);
                padding: 30px 25px;
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                box-shadow: 0 4px 15px rgba(0,0,0,0.3), 0 0 25px rgba(0,255,255,0.1);
                backdrop-filter: blur(10px);
                text-align: center;
                max-width: 330px;
                width: 90%;
            }

            h1 {
                font-size: 1.3rem;
                margin-bottom: 18px;
                color: #00f0ff;
                text-shadow: 0 0 8px #00f0ff;
            }

            p {
                font-size: 0.95rem;
                margin-bottom: 15px;
                color: #fff;
                text-shadow: 0 0 3px rgba(255,255,255,0.2);
            }

            .btn {
                display: inline-block;
                padding: 12px 26px;
                background-color: #00d5ff;
                color: #fff;
                text-decoration: none;
                border-radius: 12px;
                font-weight: bold;
                box-shadow: 0 0 12px #00eaff, 0 0 22px #00eaff;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }

            .btn:hover {
                transform: scale(1.05);
                box-shadow: 0 0 20px #00eaff, 0 0 30px #00eaff;
            }

            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background: rgba(0, 0, 0, 0.4);
                text-align: center;
                padding: 10px 0;
                font-size: 0.9rem;
                color: #ccc;
            }

            .footer a {
                color: #00f0ff;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✅ Uptime Pinger is Running! 🚀</h1>
            <p>📢 Join our channel:</p>
            <a href="https://t.me/Opleech_WD" class="btn" target="_blank">@Opleech_WD</a>
            <p>🔔 Stay tuned for upcoming features & updates!</p>
        </div>

        <div class="footer">🤍 Developed by <a href="#">Sanchit</a></div>
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
