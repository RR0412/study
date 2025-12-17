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

        else:
            response.add_header('Content-Type', 'text/html')
            response.add_header('Connection','close')
            response.set_status(Response.HTTP_NOT_FOUND)
            response.set_body('<h1>Not Found!</h1>')
        
        return response.send()

class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

HOST, PORT = "localhost", 5555
TCPServer.allow_reuse_address = True

with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()
