# Importing necessary libraries
import os
from os import system as _sys 
import time
from time import sleep as wait
import json
import urllib.request

# Load configuration files
with open('config/config.json') as f:
    cfg = json.load(f)
    APP_NAME = cfg['AppName']
    DEV = cfg['Developer']
    USERNAME_LIST = cfg['login']['username']
    PASSWORD = cfg['login']['password']
    IS_REQUIRED_TO_LOGIN = cfg['login']['isRequiredToLogin']
    HOSTNAME = cfg['server_database']['server_hostname']
    PORT = cfg['server_database']['serverPort']
    USE_SERVER = cfg['server_database']['useServer']

# Create a class to handle login event
class loginEvent():
    # Define a function to read file
    def readFile(filename):
        file = open(filename, 'r', encoding='utf-8')
        content = file.read()
        print(content)
        file.close()
    # Define a function to load login event
    def createLogin():
        if IS_REQUIRED_TO_LOGIN:
            _sys('cls')
            _sys('title Orion Login')
            if USE_SERVER:
                username = input('Username: ')
                username_edit = username.lower()
                with urllib.request.urlopen('http://{}:{}/database/{}.json'.format(HOSTNAME, PORT, username_edit)) as url:
                    data = json.load(url)
                    LOGIN_USERNAME = data['username']
                    LOGIN_PASSWORD = data['password']
                    if username == LOGIN_USERNAME:
                        password = input('Password: ')
                        if password == LOGIN_PASSWORD:
                            print('Login successfull, redirecting to {} in 5 seconds...'.format(APP_NAME))
                            wait(5)
                            return True
                        else:
                            return False
                    else: 
                        return False
                        
