# Importing necessary libraries
import json
import os, sys
from os import system as _sys 
from pathlib import Path
import json

# Object

# Creating a class to handle necessary function
class DatabasePanel():
    def __init__(self):
        _sys('title Orion Database Manager')
        _sys('cls')
    def commandParse(self, command):
        if command == "createaccount":
            username = input('Account Username: ')
            password = input('Account Password: ')
            if username == None or password == None:
                return
            file = Path('../server/database/{}.json'.format(username.lower()))
            if file.is_file():
                print('File data: {} already exists'.format(username))
            else:
                json_object = {
    "username": "{}".format(username),
    "password": "{}".format(password)
}
                jsonstring = json.dumps(json_object)
                data_file = open('../server/database/{}.json'.format(username.lower()), 'w')
                data_file.write(jsonstring)
                data_file.close()
                print('Database: {} has been created'.format(username))
    def run(self):
        while True:
            self.commandParse(input('database > '))
            
if __name__ == "__main__":
    app = DatabasePanel()
    app.run()
