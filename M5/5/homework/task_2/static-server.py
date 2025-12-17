from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn
from request import Request
from response import Response
from static_responder import StaticResponder
import mimetypes

class MyTCPHandler(StreamRequestHandler):

    def handle(self):
        request = Request(self.rfile)
        response = Response(self.wfile)
        static_responder = StaticResponder(request, response, 'static')
        if static_responder.file:
            content_type, _ = mimetypes.guess_type(static_responder.file)
            if content_type:
                response.add_header('Content-Type', content_type)
            else:
                response.add_header('Content-Type', 'application/octet-stream')
            
            response.add_header('Connection', 'close')
            static_responder.prepare_response()
            response.send()
            return
        else:
            if request.uri == '/' :
                response.body = b'<a href="/one">First page</a><br/>\n<a href="/two">Second page</a><br/>\n<a href="/three">Third page</a><br/>\n'
            elif request.uri == '/one':
                response.body = b'<h1>This is first page!</h1>'
            elif request.uri == '/two':
                response.body = b'<h2>This is second page!</h2>'
            elif request.uri == '/three':
                response.body = b'<h3>This is third page!</h3>'
            else:
                response.status = response.HTTP_NOT_FOUND
                response.body = b'<h1>Not found</h1>'
        
            response.add_header('Content-Type', 'text/html')
            response.add_header('Connection','close')
            response.send()

class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

HOST, PORT = "localhost", 5555
TCPServer.allow_reuse_address = True

with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()
