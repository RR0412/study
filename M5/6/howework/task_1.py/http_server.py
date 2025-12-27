from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn
from request import Request
from response import Response
from static_responder import StaticResponder
import os
from pages import PagesController
from posts import PostsController
from errors import not_found
from router import Router

router = Router()
router.get('/', PagesController, 'home_page')
router.get('/first_page',PagesController, 'first_page')
router.get('/second_page', PagesController, 'second_page')
router.get('/third_page', PagesController, 'third_page')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        request = Request(self.rfile)
        response = Response(self.wfile)
        static_responder = StaticResponder(request, response, STATIC_DIR)

        if static_responder.file:
            static_responder.prepare_response()

        else:
            response.add_header('Content-Type', 'text/html')
            response.add_header('Connection', 'close')
            router.run(request,response)
                            
        response.send()


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

HOST, PORT = "localhost", 5555
TCPServer.allow_reuse_address = True

with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()
