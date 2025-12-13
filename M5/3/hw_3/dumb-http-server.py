from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn
from request import Request

class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        request = Request(self.rfile)
        
        print('Method: ', request.method)
        print('Uri: ', request.uri)
        print('Protocol:', request.protocol)

        if request.uri == '/':
            response_body = '<h1>Follow the white rabbit.</h1>'
            response_body_length = len(response_body.encode())
            response = [
                'HTTP/1.1 200 OK',
                'Content-Type: text/html',
                'Content-Length: ' + str(response_body_length),
                'Connection: close',
                '',
                response_body
            ]


        elif request.uri == '/white_rabbit' : 
            response_body = '<h1 style="color: white;">You are living in the matrix.</h1>'
            response_body_length = len(response_body.encode())
            response = [
            'HTTP/1.1 200 OK',
            'Content-Type: text/html',
            'Content-Length: ' + str(response_body_length),
            'Connection: close',
            '',
            response_body
        ]
        else:
            response_body = '<h1>501 Not implemented</h1>'
            response_body_length = len(response_body.encode())
            response = [
                'HTTP/1.1 501 Not implemented',
                'Content-Type: text/html',
                'Content-Length: ' + str(response_body_length),
                'Connection: close',
                '',
                response_body
            ]

        self.wfile.write('\r\n'.join(response).encode())

class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

HOST, PORT = "localhost", 2000
TCPServer.allow_reuse_address = True

with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()
