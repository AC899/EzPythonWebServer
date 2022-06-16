from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"   #self-explanatory - local host

#unit test - error message when ports are over 65,535

valid = False
while not valid: #loop until the user enters a valid int
    try:
        x = int(input('Welcome to EZ Python Webserver \nEnter the port number for your webserver i.e. 8000'))  #Enter port you wish to use
        valid = True                         #if this point is reached, x is a valid int
    except ValueError:
        print('Please only input digits')    #Error message for not inputting digits
    except OverflowError as err:
        print('Overflowed after ', err)
    else:
        serverPort = x

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")