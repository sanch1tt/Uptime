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
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: #fff;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            .outer-container {
                background: rgba(255, 255, 255, 0.05);
                padding: 20px;
                border-radius: 20px;
                border: 2px solid #fff;
                box-shadow: 0 8px 25px rgba(0,0,0,0.4), 0 0 40px rgba(255,255,255,0.2);
                backdrop-filter: blur(8px);
                width: 100%;
                max-width: 450px;
            }
            .inner-container {
                background: rgba(255, 255, 255, 0.1);
                padding: 20px;
                border-radius: 15px;
                border: 1px solid rgba(255,255,255,0.3);
                box-shadow: inset 0 2px 10px rgba(0,0,0,0.3);
                text-align: center;
            }
            .heading {
                font-size: 1.8rem;
                margin-bottom: 18px;
                color: #00f2fe;
                text-shadow: 2px 2px 5px #000, 0 0 10px #00f2fe;
            }
            .subheading, .updates {
                margin-bottom: 12px;
                font-size: 1rem;
                text-shadow: 1px 1px 3px #000;
            }
            .subheading {
                color: #f9ca24;
            }
            .updates {
                color: #e056fd;
            }
            .btn {
                display: inline-block;
                padding: 12px 22px;
                background: linear-gradient(145deg, #6dd5ed, #2193b0);
                color: #fff;
                text-decoration: none;
                border-radius: 8px;
                box-shadow: 0 6px 12px rgba(0,0,0,0.3);
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                font-weight: bold;
                margin-bottom: 15px;
            }
            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 16px rgba(0,0,0,0.4);
            }
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                padding: 8px 0;
                background: rgba(0,0,0,0.4);
                text-align: center;
                color: #fff;
                font-size: 0.85rem;
                box-shadow: 0 -2px 10px rgba(0,0,0,0.4), 0 0 10px rgba(255,255,255,0.2);
                backdrop-filter: blur(5px);
                text-shadow: 1px 1px 3px #000;
            }
            .footer a {
                color: #6dd5ed;
                text-decoration: none;
                font-weight: bold;
            }
            .footer a:hover {
                color: #00f2fe;
                text-decoration: underline;
            }
            @media (max-width: 400px) {
                .heading { font-size: 1.5rem; }
                .btn { padding: 10px 18px; }
            }
        </style>
    </head>
    <body>
        <div class="outer-container">
            <div class="inner-container">
                <div class="heading"><i class="fas fa-check-circle"></i> Uptime Pinger is Running! <i class="fas fa-rocket"></i></div>
                <div class="subheading"><i class="fas fa-bullhorn"></i> Join our channel:</div>
                <a href="https://t.me/Opleech_WD" class="btn" target="_blank"><i class="fab fa-telegram-plane"></i> @Opleech_WD</a>
                <div class="updates"><i class="fas fa-bell"></i> Stay tuned for upcoming features & updates!</div>
            </div>
        </div>
        <div class="footer">
            <i class="fas fa-heart"></i> Developed by <a href="https://t.me/S4NCHITT" target="_blank">𝐒𝐚𝐧𝐜𝐡𝐢𝐭</a>
        </div>
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
