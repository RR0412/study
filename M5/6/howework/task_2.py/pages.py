from controller import Controller

class PagesController(Controller):
    Counter = 0
    def home_page(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<h1 style="font-size: 5em;">0</h1>'
        '<a href="/click"><button>Click</button></a>')

