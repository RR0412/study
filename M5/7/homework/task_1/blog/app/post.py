from http_fw.controller import Controller
from db import Database

class PostController(Controller):
    def index(self):
        posts = Database.find()

        body = '<h1>This is posts page!</h1>'

        for post in posts:
            body +=  f"<a href='/post?id={post['id']}'><h3>{post['title']}</h3></a>"

        body += "<a href='/posts/new'>Add new post</a>"

        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)

    def new(self):
        body = '''<form action="/posts" method="POST">
        <h1>Create new post!</h1>
        <label>
        Title: <input type="text" name="title" />
        </label>
        <br/>
        <label>
        Description: <textarea name="description"></textarea>
        </label>
        <br/>
        <input type="submit" value="Create!"/>
        <br/>
        <a href="/">Return to main page</a>
        </form>
        '''

        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)

    def create(self):
        Database.counter+=1 
        post = {
            'id': Database.counter,
            'title': self.request.body['title'][0],
            'description': self.request.body['description'][0]
        }

        Database.add(post)
        Database.counter+=1 

        self.response.set_status(301)
        self.response.add_header('Location', '/')
        print("Request body:", self.request.body)
        print("New post:", post)

    def view_post(self):
        id = int(self.request.query['id'][0])
        post = Database.find_by_id(id)
        body = f'<h2>This is post title<br/> {post["title"]}</h2><br/>This is post description<br/> {post["description"]}'
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)


    


