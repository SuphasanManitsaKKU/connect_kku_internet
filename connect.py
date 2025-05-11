import time
import requests
from dotenv import load_dotenv
import os
import random
import json
import threading
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

load_dotenv()

fail = 0
status = "ok"
log_file = "fail_log.json"
current_count = 0

# Initialize the log file if not exists
if not os.path.exists(log_file):
    with open(log_file, 'w') as f:
        json.dump({
            "status": "ok",
            "total_count": 0,
            "logs": []
        }, f, indent=2)

# Load total_count ตอนเริ่มสคริปต์
with open(log_file, 'r') as f:
    data = json.load(f)
    current_count = data.get("total_count", 0)

check_list = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.instagram.com",
    "https://www.linkedin.com",
    "https://www.github.com",
    "https://www.medium.com",
    "https://www.stackoverflow.com",
    "https://www.wikipedia.org",
    "https://www.apple.com",
    "https://www.microsoft.com",
    "https://www.spotify.com",
    "https://www.cnn.com",
    "https://www.bbc.com",
    "https://www.nytimes.com",
    "https://www.oracle.com",
    "https://www.ibm.com",
    "https://www.intel.com",
    "https://www.mozilla.org",
    "https://www.cloudflare.com",
    "https://www.paypal.com",
    "https://www.quora.com",
    "https://www.booking.com",
    "https://www.tiktok.com",
    "https://www.ebay.com",
    "https://www.pinterest.com",
    "https://www.shopify.com",
    "https://www.samsung.com",
    "https://www.huawei.com",
    "https://www.sony.com",
    "https://www.dell.com",
    "https://www.lenovo.com",
    "https://www.dropbox.com",
    "https://www.slack.com",
    "https://www.atlassian.com",
    "https://www.trello.com",
    "https://www.theguardian.com",
    "https://www.bloomberg.com",
    "https://www.target.com",
    "https://www.ikea.com",
    "https://www.nordstrom.com",
    "https://www.sephora.com",
    "https://www.abcnews.go.com",
    "https://www.usatoday.com",
    "https://www.vox.com",
    "https://www.npr.org",
    "https://www.ted.com",
    "https://www.khanacademy.org",
    "https://www.coursera.org",
    "https://www.udemy.com",
    "https://www.edx.org",
    "https://www.freecodecamp.org",
    "https://www.bitbucket.org",
    "https://www.digitalocean.com",
    "https://www.heroku.com",
    "https://www.wordpress.com",
    "https://www.wix.com",
    "https://www.zoho.com",
    "https://www.hubspot.com"
]

def log_fail():
    global current_count
    with open(log_file, 'r+') as f:
        data = json.load(f)
        logs = data.get("logs", [])
        current_count += 1

        new_log = {
            "count": current_count,
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

        logs.insert(0, new_log)

        data = {
            "status": "no ok",
            "total_count": current_count,
            "logs": logs
        }

        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

def log_status_ok():
    with open(log_file, 'r+') as f:
        data = json.load(f)
        data["status"] = "ok"
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

def check_internet_connection():
    try:
        response = requests.get(random.choice(check_list), timeout=3)
        return True
    except:
        return False

def enable():
    try:
        login_url = "https://nac10.kku.ac.th/login"
        login_data = {
            'username': os.getenv('KKU_USERNAME'),
            'password': os.getenv('KKU_PASSWORD'),
        }
        response = requests.post(login_url, data=login_data)
        if "You are logged in" in response.text:
            print("connected")
        else:
            print("can't connect")
    except:
        pass

def internet_monitor():
    global fail, status
    while True:
        if not check_internet_connection():
            status = "no ok"
            fail += 1
            log_fail()
            enable()
        else:
            status = "ok"
            log_status_ok()

        print("\033c", end="")
        print(f'Status : {status}')
        print(f'Fail : {fail}')
        time.sleep(1)

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            try:
                with open(log_file, 'r') as f:
                    data = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(data)))
                self.end_headers()
                self.wfile.write(data.encode())
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'Internal Server Error')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

def run_server():
    server_address = ('', 80)
    httpd = HTTPServer(server_address, SimpleHandler)
    print('Server running at http://localhost:80/')
    httpd.serve_forever()

# ---------------------- START MAIN -----------------------

if __name__ == "__main__":
    t1 = threading.Thread(target=internet_monitor)
    t2 = threading.Thread(target=run_server)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

# cp .env.example .env
# pip install -r requirements.txt