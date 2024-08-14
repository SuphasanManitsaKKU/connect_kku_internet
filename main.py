from playwright.sync_api import sync_playwright
import time
import os
import requests
import csv
from datetime import datetime
from dotenv import load_dotenv
import os

# -------------------------------------------------------------------------------------------------------------------------------------------------------
# do_you_test = True or False
do_you_test = False
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Load environment variables from .env file
load_dotenv()
# Access the variables

try:
    username = os.getenv("U_U")
    password = os.getenv("S_S")
    if username == None and password == None:
        username = os.getenv("USERNAME_ENV")
        password = os.getenv("PASSWORD_ENV")
        if username == None and password == None:
            print("what the fuck")
            exit()
except:
    print("what the fuck")
    exit()

def log(inp: str):
    if do_you_test:
        pass

    with open('log.csv', 'a', newline='') as file:
        file_write = csv.writer(file)
        current_date_time = datetime.now()
        file_write.writerow([str(current_date_time) + ": " + inp])

print(f"username: {username} password: {password}")
log(f"username: {username} password: {password}")

def enable(inp:str):
    try:
        # URL of the login form's action
        login_url = "https://nac10.kku.ac.th/login"

        # Data to be sent with the POST request
        login_data = {
            'username': username,
            'password': password,
        }

        # Send the POST request
        response = requests.post(login_url, data=login_data)

        # Check if the login was successful
        if "You are logged in" in response.text:
            print(f"{inp}: internet connect: connected")
            log("internet connect: connected")
        else:
            a = 0 / 0

    except:
        print(f"{inp}: internet connect: error can't connect")
        log("internet connect: error can't connect")

def check_internet_connection(inp:str,count:int):
    try:
        response = requests.get("https://www.google.com", timeout=1)

        print(f"{inp}: internet connect: ok : count = ({count})")
        log(f"internet connect: ok : count = ({count})")
        return True,count
    except:
        count += 1

        print(f"{inp}: internet connect: disconnected : count = ({count})")
        log(f"internet connect: disconnected : count = ({count})")
        return False,count

count = 0

while(True):
    current_date_time = str(datetime.now())
    condition,count = check_internet_connection(current_date_time,count)
    if condition == False:
        enable(current_date_time)
    time.sleep(5)