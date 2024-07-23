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

def start():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    # browser = playwright.chromium.launch(headless=False)
    return [playwright,browser]

def enable(inp:str):
    try:
        [playwright,browser] = start()
        page = browser.new_page()
        page.goto("https://login.kku.ac.th/")
        page.locator("#username").click()
        page.keyboard.type(f"{username}",delay=10)
        page.keyboard.press("Tab")
        page.keyboard.type(f"{password}",delay=10)
        page.keyboard.press("Enter")
        time.sleep(1)
        playwright.stop()

        print(f"{inp}: internet connect: connected")
        log("internet connect: connected")
    except:
        print(f"{inp}: internet connect: error can't connect")
        log("internet connect: error can't connect")

def disable(inp:str):
    try:
        [playwright,browser] = start()
        page = browser.new_page()
        page.goto("https://login.kku.ac.th/status")
        page.locator("#btnLogOff").click()
        time.sleep(1)
        playwright.stop()

        print(f"{inp}: internet connect: disconnected")
        log("internet connect: disconnected")
    except:
        print(f"{inp}: internet connect: error can't disconnect")
        log("internet connect: error can't disconnect")

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