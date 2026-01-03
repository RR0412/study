from http_fw.controller import Controller
from db import Database
    
class AdsController(Controller):
    def index(self):
        ads = Database.find()
        body = """
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body>
            <h1>Cars Dealership</h1>
        """
        for ad in ads:
            body += f"""
            <div class="container">
            <img src = "{ad["image"]}" class="image-left front-photo" alt = "Add picture should be here">
            <p><a href="/ad?id={ad['id']}">{ad["mark"]} ({ad["year"]})</a>
            <br>${ad["price"]}</p>
            </div>
            """

        body+= '<br><a href="http://localhost:9000/ads/new">Place new advertisement</a>'
   

        self.response.add_header('Content-type','text/html')
        self.response.set_body(body)

    def new(self):
        body = '''<form action="/ads" method="POST">
        <h1>Place new advertisement</h1>
        <label for="mark">Mark </label>
        <select id="mark" name="mark">
        '''
        for mark in Database.MARKS:
            body += f'<option value = "{mark}">{mark}</option>'
        body += '</select>'
        body += '''<br/>
        <label>
        Year <input type="number" name="year">
        </label>
        <br/>
        <label>
        Price <input type="number" name="price">
        </label>
        <br/>
        <label>
        Image <input type="text" name="image">
        </label>
        <br/>
        <label>
        Description <textarea name="description"></textarea>
        </label>
        <br/>
        <label>
        Contacts <textarea name="contacts"></textarea>
        </label>
        <button type="submit">Create</button>
        </form>                 
        <br/>
        <a href="http://localhost:9000/ads">Return to home page</a>
        '''
        self.response.add_header('Content-type', 'text/html')
        self.response.set_body(body)

    def create(self):
        Database.COUNTER+=1
        ad = {
            'id': Database.COUNTER,
            'mark':self.request.body['mark'][0],
            'year':int(self.request.body['year'][0]),
            'price':int(self.request.body['price'][0]),
            'image':self.request.body['image'][0],
            'description':self.request.body['description'][0],
            'contacts':self.request.body['contacts'][0]
        }

        Database.add(ad)
        self.response.set_status(301)
        self.response.add_header('Location', '/ads')

    def ad(self):
        if 'id' not in self.request.query:
            self.response.set_body('No ad id provided')
            return
        id = int(self.request.query['id'][0])
        ad = Database.find_by_id(id)

        if not ad:
            self.response.set_body('Ad not found')
            return
        body = f'''
        <html>
        <head>
            <link rel="stylesheet" href="/static/style.css>
        </head>
        <body>
            <h1>View advertisement</h1><br/>
            <img src="{ad['image']}" class="front-photo"><br/>

            <b>Mark:</b> {ad['mark']}<br/>
            <b>Year:</b> {ad['year']}<br/>
            <b>Description:</b> {ad['description']}<br/>
            <b>Contact:</b> {ad['contacts']}<br/>

            <a href="http://localhost:9000/ads">Return to home page</a>
        </body>
        </html>       
'''
        self.response.add_header('Content-type', 'text/html')
        self.response.set_body(body)      
        