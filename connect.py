import time
import requests
import os

fail = 0
status = "ok"
def check_internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=1)
        return True
    except:
        return False

def enable():
    try:
        login_url = "https://nac10.kku.ac.th/login"

        # Data to be sent with the POST request
        login_data = {
            'username': os.getenv('USERNAME'),
            'password': os.getenv('PASSWORD'),
        }

        # Send the POST request
        response = requests.post(login_url, data=login_data)

        # Check if the login was successful
        if "You are logged in" in response.text:
            print("ok")
        else:
            print("error")
    except:
        pass

while(True):
    if check_internet_connection() == False:
        status = "no ok"
        fail += 1
        enable()
    else:
        status = "ok"
    os.system("clear")
    print(f'Status : {status}')
    print(f'Fail : {fail}')
    time.sleep(5)
