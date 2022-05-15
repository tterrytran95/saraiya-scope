# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os 

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def create_page(self):
        page = '''
        <!DOCTYPE html>
        <html>
        <body>

        <img src="server/hello.jpeg">
        <p>hello</p>

        </body>
        </html>
        '''
        return page
        
    def send_page(self, page):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(bytes(page, "utf-8"))
        
    def update_page(self, image_name):
        page = '''
        <!DOCTYPE html>
        <html>
        <body>

        <img src="server/frames/{}">
        <p>hello,{}</p>
        </body>
        </html>
        '''.format(image_name, image_name)
        return page
        
    def do_GET(self):
        page = self.create_page() 
        self.send_page(page)
        n = 0 
        image_name = "frame0.jpg"
        images = os.listdir('server/frames')
        # print(images)
        while n < 10:
            time.sleep(5)
            image_name = images[n]
            n += 1
            page = self.update_page(image_name)
            self.send_page(page)
        
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")