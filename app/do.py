from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import requests

# system imports
import os
import sys

connectionString = None
data = None


def init(cityId):
    global connectionString
    global data
    print("\napi - init\n")

    # Build connectiong string
    connectionString = "https://api.openweathermap.org//data/2.5/weather?id=" + \
        cityId+"&units=metric&appid=244df0cbb2bcae2bca2fbe929ae3a613"
    data = requests.get(connectionString).json()


class ServiceHandler(BaseHTTPRequestHandler):
    # sets basic headers for the server
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        # reads the length of the Headers
        length = int(self.headers['Content-Length'])
        # reads the contents of the request
        content = self.rfile.read(length)
        temp = str(content).strip('b\'')
        self.end_headers()
        return temp

    ######
    #LIST#
    ######
    # GET Method Definition
    def do_GET(self):
        #obtain user input for cityID
        temp = self._set_headers()
        init(temp)

        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
        


# Server Initialization
server = HTTPServer(('127.0.0.1', 8080), ServiceHandler)
server.serve_forever()