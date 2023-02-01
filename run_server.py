import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 443
CERT_FILE = "./public-key.crt"
PRIVATE_KEY = "./private-key.pem"

Handler = SimpleHTTPRequestHandler

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(CERT_FILE, PRIVATE_KEY)

with HTTPServer(("", PORT), Handler) as httpd:
    print("serving at address", httpd.server_address)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()