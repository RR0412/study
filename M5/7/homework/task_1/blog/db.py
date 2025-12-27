class Database:
    counter = 2
    posts = [{
        'id': 1,
        'title' : 'This is my first post!',
        'description': 'This is test description!'
    },{
        'id': 2,
        'title': 'Hey, I did something new!',
        'description': 'This is another description!'
    }]

    @staticmethod
    def find():
        return Database.posts
    
    @staticmethod
    def add(post):
        Database.posts.append(post)

    @staticmethod
    def find_by_id(id):
        for post in Database.posts:
            if post['id'] == id:
                return post
        else:
            return None



           





