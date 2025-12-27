from controller import Controller

class PagesController(Controller):
    def home_page(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<a href="/first_page">First page</a><br>' 
        '<a href="/second_page">Second page</a><br/>' 
        '<a href="/third_page">Third page</a><br/>')


        
    def first_page(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<h1>This is first page</h1>')

    def second_page(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<h1>This is second page</h1>')

    def third_page(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<h1>This is third page</h1>')


