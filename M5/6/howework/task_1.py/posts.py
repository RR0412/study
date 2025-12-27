from controller import Controller

class PostsController(Controller):
    def index(self):
        posts_db = [{'id': 1, 'title': 'This is first post'},
                    {'id': 2, 'title': 'This is second post'},
                    {'id': 3, 'title': 'This is third post'}
        ]

        body = '<h1>This  is posts page!</h1>'

        for post in posts_db:
            body += f"<h3>{post['title']} (ID: {post['id']})</h3>"
        
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)