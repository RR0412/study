from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn
from .request import Request
from .response import Response
from .static_responder import StaticResponder

class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

def run(router, config):
    class TCPHandler(StreamRequestHandler):
        def handle(self):
            request = Request(self.rfile)
            response = Response(self.wfile)
            response.add_header('Connection', 'close')

            static = StaticResponder(request, response, config['static'])

            if static.file:
                static.prepare_response()
            else:
                if request.method == 'POST':
                    request.parse_body()
                router.run(request, response)

            response.send()
    
    TCPServer.allow_reuse_address = True
    address = (config['host'], config['port'])

    with ThreadedTCPServer(address, TCPHandler) as server:
        server.serve_forever()
        