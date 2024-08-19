import time
import requests

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
            'username': "6533801529",
            'password': "Mikuto0807494698",
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
        enable()
    time.sleep(5)
