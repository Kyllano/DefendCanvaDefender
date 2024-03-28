from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
import json

class myHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        #self.send_header("Last-Modified", self.date_time_string(time.time()))
        #self.end_headers()
        return SimpleHTTPRequestHandler.do_GET(self)

        

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself
        data = json.loads(post_data)
        print("coucou", data)

        


httpd = HTTPServer(('', 8080), myHTTPRequestHandler)

httpd.serve_forever()