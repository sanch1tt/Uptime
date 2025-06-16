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
                body {
                    margin: 0;
                    padding: 0;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                    color: #fff;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .container {
                    background: rgba(255, 255, 255, 0.05);
                    padding: 40px 30px;
                    border-radius: 15px;
                    border: 2px solid #fff;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.3), 0 0 30px rgba(255,255,255,0.2);
                    backdrop-filter: blur(10px);
                    max-width: 400px;
                    text-align: center;
                }
                h1 {
                    font-size: 2rem;
                    margin-bottom: 20px;
                    text-shadow: 2px 2px 5px #000;
                }
                p {
                    margin-bottom: 20px;
                    font-size: 1.1rem;
                    text-shadow: 1px 1px 3px #000;
                }
                .btn {
                    display: inline-block;
                    padding: 12px 24px;
                    background: linear-gradient(145deg, #6dd5ed, #2193b0);
                    color: #fff;
                    text-decoration: none;
                    border-radius: 8px;
                    box-shadow: 0 6px 12px rgba(0,0,0,0.3);
                    transition: transform 0.2s ease, box-shadow 0.2s ease;
                    font-weight: bold;
                }
                .btn:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 8px 16px rgba(0,0,0,0.4);
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
        </body>
        </html>
    '''
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
