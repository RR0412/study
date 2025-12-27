from controller import Controller
from pages import PagesController

class CountController(Controller):
    def clicker(self):
        PagesController.Counter +=1
        body = f'<h1 style="font-size: 5em;">{PagesController.Counter}</h1><a href="/click"><button>Click</button></a>'
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)