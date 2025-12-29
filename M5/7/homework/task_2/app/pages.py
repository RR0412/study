from http_fw.controller import Controller

class PagesController(Controller):
    def home(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<h1>This is homepage</h1>')

    def about(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<h1>This is about page</h1>')


