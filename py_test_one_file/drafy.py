
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3
import json

con = sqlite3.connect('file.db')
cur = con.cursor()

# cur.execute("INSERT INTO files VALUES ('gil','aaabgyftyfaaaaaaaaa')")
files = []
for row in cur.execute("SELECT * FROM files"): # print(row) # print(row[0], row[1])
    currFile = {
        'name': row[0],
        'fileSrc': row[1]
    }
    files.append(currFile)
con.commit()
# con.close()


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self._set_headers()
            # self.wfile.write(self._html("hia!"))
            print('in get')
            if(self.path == '/'):# in case that have to drow all the data (start)
                # have to send the data to the front!!
                # self.wfile.write(self._html(files))
                cur.execute("SELECT * FROM files")
                self.wfile.write(b'Hello, world!')
                # print(json.dumps(files))
                return (json.dumps(files))
            # in case that have to drow spacific file name
            cur.execute("SELECT * FROM files")
            aaaa = self.path
            print(aaaa)
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self._set_headers()
        print('in post')
        post_data = (self.rfile.read(int(self.headers['content-length']))).decode('utf-8')
        startIndex = post_data.index('&fileSrc=')
        updateStertIdx = startIndex+9
        fileName = post_data[:startIndex]
        fileSrc = post_data[updateStertIdx:]
        cur.execute("INSERT INTO files (name, fileSrc) VALUES(?, ?)",(fileName, fileSrc))
        self.wfile.write(self._html(files))
        # print(json.dumps(files))
        con.close()
        # missing a command to send te db!
        self._set_headers()


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=3040):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


def serve_forever(self):
    while not self.stopped:
        self.handle_request()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=3040,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)
