from http_fw.controller import Controller
from db import Database
from datetime import datetime

class TaskController(Controller):
    def index(self):
        tasks = Database.find()
        body = '<h1>This is tasks page!</h1>'
        for task in tasks:
            body += f"<a href='/task?id={task['id']}'><h3>{task['title']}</h3></a><br/><h2>{task['created_at']}</h2>"

        body += '<a href="/tasks/new">Add new task</a>'

        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)

    def new(self):
        body = '''<form action="/tasks" method="POST">
        <h1>Create new task!</h1>
        <label>
        Title: <input type="text" name="task" />
        </label>
        <br/>
        <label>
        Description: <textarea name="task_description"></textarea>
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
        Database.counter +=1
        task = {
            'id': Database.counter,
            'title': self.request.body['task'][0],
            'description': self.request.body['task_description'][0],
            'created_at': datetime.now().strftime("%d.%m.%Y %H:%M"),
        }

        Database.add(task)

        self.response.set_status(301)
        self.response.add_header('Location', '/tasks')

    def view_task(self):
        id = int(self.request.query['id'][0])
        task = Database.find_by_id(id)
        body = f'<h2> Task title<br/>{task["title"]}<br/>Task description:<br/>{task["description"]}<br/>Created at:<br/> {task["created_at"]}</h2>'
        
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)
