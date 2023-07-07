# Orion server handler
# Used to host several database to a server.

# Importing necessary libraries
import http.server
import socketserver
import os, sys
import json
import time
from time import sleep as wait
from pathlib import Path

# Configuration files
root_folder = Path(__file__).parents[2]

my_path = root_folder / "source/config/config.json"
with open(my_path) as config:
    cfg = json.load(config)
    PORT = cfg['server_database']['serverPort']
    USE_SERVER = cfg['server_database']['useServer']
    APP_NAME = cfg['AppName']

# Create a class to handle server-need functions
class serverHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        data_path = '../database/'
        if self.path == "/database/":
            for r, d, f in os.walk(data_path):
                for file in f:
                    if file.endswith('.json'):
                        print(os.path.join(r, file))
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

class serverFunction():
    def createServerPath(PORT):
        handler_object = serverHandler
        server_url = socketserver.TCPServer(("", PORT), handler_object)
        print('[STARTUP] Starting up {} HTTP server on port: {}'.format(APP_NAME, str(PORT)))
        wait(3)
        print('[SERVER] {} HTTP server has been started'.format(APP_NAME))
        server_url.serve_forever()
        
if __name__ == "__main__":
    serverFunction.createServerPath(PORT)
