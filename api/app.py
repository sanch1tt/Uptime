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
                background: linear-gradient(160deg, #0f2027, #203a43, #2c5364);
                color: white;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                position: relative;
            }

            .container {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255,255,255,0.4);
                padding: 25px 20px;
                border-radius: 15px;
                box-shadow: 0 0 15px rgba(255,255,255,0.2), 0 4px 30px rgba(0,0,0,0.5);
                backdrop-filter: blur(10px);
                max-width: 340px;
                width: 90%;
                text-align: center;
            }

            h1 {
                font-size: 1.4rem;
                margin-bottom: 15px;
                color: #00eaff;
                text-shadow: 0 0 8px #00eaff;
            }

            p {
                margin: 10px 0;
                font-size: 1rem;
                text-shadow: 0 0 3px rgba(255,255,255,0.4);
            }

            .btn {
                display: inline-block;
                background-color: #00bfff;
                padding: 12px 22px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: bold;
                color: white;
                box-shadow: 0 0 10px #00bfff, 0 0 20px #00bfff;
                transition: 0.2s ease-in-out;
                margin-bottom: 10px;
            }

            .btn:hover {
                transform: scale(1.05);
                box-shadow: 0 0 15px #00eaff, 0 0 25px #00eaff;
            }

            .footer {
                position: absolute;
                bottom: 10px;
                font-size: 0.85rem;
                color: #aaa;
                text-align: center;
                width: 100%;
            }

            .footer a {
                color: #00eaff;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✅ Uptime Pinger is Running! 🚀</h1>
            <p>📢 Join our channel:</p>
            <a class="btn" href="https://t.me/Opleech_WD" target="_blank">@Opleech_WD</a>
            <p>🔔 Stay tuned for upcoming features & updates!</p>
        </div>

        <div class="footer">❤️ Developed by <a href="#">Sanchit</a></div>
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
