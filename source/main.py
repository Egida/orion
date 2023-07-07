# Importing necessary libraries
import os
from os import system as _sys
import sys
import time
from time import sleep as wait
import json
from src.func.event.loginEvent import *
from src.func.handler.attackEvent import *
import threading
from src.func.handler.commandHandler import *

# Configuration variable
with open('config/config.json') as f:
    cfg = json.load(f)
    APP_NAME = cfg['AppName']
    DEV = cfg['Developer']
    METHOD_LIST = cfg['attack']['method_list']
    IS_REQUIRED_TO_LOGIN = cfg['login']['isRequiredToLogin']

# Creating a class to handle related functions
class Orion():
    # Creating a function to initialize several system
    def __init__(self):
        _sys('cls')
        _sys('title Orion V2')
    # Define a function to handle command usage
    def commandParser(self, command):
        cmdHandler.parseCmd(command)
    def run(self):
        cmdHandler.graphics('src/assets/interface/graphic.txt')
        try:
            while True:
                _prompt = cmdHandler.readFileContent('src/assets/interface/prompt.txt')
                self.commandParser(input(_prompt))
        except KeyboardInterrupt:
            print('\nLeaving {} in 5 seconds...'.format(APP_NAME))
            wait(5)
            exit()
            
# Main functions
if __name__ == "__main__":
    if loginEvent.createLogin():
        app = Orion()
        app.run()
    elif IS_REQUIRED_TO_LOGIN == False:
        app = Orion()
        app.run()
