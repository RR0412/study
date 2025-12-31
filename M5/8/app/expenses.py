from http_fw.controller import Controller
from db import Database

class ExpensesController(Controller):
    def index(self):
        expenses = Database.find()
        body = '<h1>Expense Tracker</h1>'
        for expense in expenses:
            body += f'Category:{expense["category"]}, Description:{expense["description"]}, Amount: {expense["amount"]}<hr>'
        total = 0
        for expense in expenses:
            total += expense['amount']
        body += f'<h3>Total expenses: {total}</h3>'
        body += '<a href="/expenses/new" style="margin-right:40px">+ Add New Expense</a>'   '<a href="/stats"> View Stats</a>'

        self.response.add_header('Content-type', 'text/html')
        self.response.set_body(body)

    def new(self):
        body = '''<form action="/expenses" method="POST">
        <h1>Add new Expense</h1>
        <label for="category">Category :</label>
        <select id="category" name="category">
        '''
        for category in Database.CATEGORIES:
            body += f'<option value ="{category}">{category}</option>'
        body += '</select>'
        body += '''<br/>
        <label>
        Description <input type="text" name="description" />
        </label>
        <br/>
        <label>
        Amount <input type="number" name="amount">
        <br/>
        </label>
        <button type="submit">Create</button>
        </form>
        '''
        self.response.add_header('Content-type','text/html')
        self.response.set_body(body)

    def create(self):
        expense = {
            'category': self.request.body['category'][0],
            'description': self.request.body['description'][0],
            'amount': int(self.request.body['amount'][0])
        }

        Database.add(expense)
        self.response.set_status(301)
        self.response.add_header('Location', '/expenses')

    def stats(self):
        food = 0
        entertainment = 0
        car = 0
        expenses = Database.find()
        for expense in expenses:
            if expense['category'] == 'Food':
                food += expense['amount']
            elif expense['category'] == 'Entertainment':
                entertainment += expense['amount']
            elif expense['category'] == 'Car':
                car += expense['amount']
        total = food + car + entertainment
        food_div = (food/total)*100
        entertainment_div = (entertainment/total)*100
        car_div = (car/total)*100 
        body = f'''
        <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
        </head>
        <body>
            <h1>Stats</h1>
            <div class="container">
                <div class="food" style="width: {food_div}%;"></div>
                <div class="entertainment" style="width: {entertainment_div}%;"></div>
                <div class="car" style="width: {car_div}%;" ></div>
            </div>
            <span class="square_food"></span> Food ( total: {food})
            <div>
            <span class="square_entertainment"></span> Entertainment ( total: {entertainment})
            </div>
            <div>
            <span class="square_car"></span> Car ( total: {car})
            </div>
            <a href="/expenses">Return to title</a>
        </body>
        </html>
        '''
        # food_green
        # entertainment_red
        # car_yellow

        self.response.add_header('Content-type','text/html')
        self.response.set_body(body)



