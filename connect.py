import time
import requests
from dotenv import load_dotenv
import os
import random

load_dotenv()

fail = 0
status = "ok"


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


def check_internet_connection():
    try:
        response = requests.get(random.choice(check_list), timeout=3)
        return True
    except:
        return False

def enable():
    try:
        login_url = "https://nac10.kku.ac.th/login"

        # Data to be sent with the POST request
        login_data = {
            'username': os.getenv('KKU_USERNAME'),
            'password': os.getenv('KKU_PASSWORD'),
        }

        # Send the POST request
        response = requests.post(login_url, data=login_data)

        # Check if the login was successful
        if "You are logged in" in response.text:
            print("connected")
        else:
            print("can't connext")
    except:
        pass

while(True):
    if check_internet_connection() == False:
        status = "no ok"
        fail += 1
        enable()
    else:
        status = "ok"
    print("\033c", end="")
    print(f'Status : {status}')
    print(f'Fail : {fail}')
    time.sleep(1)

# cp .env.example .env
# pip install -r requirements.txt