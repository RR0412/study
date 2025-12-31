class Database:
    CATEGORIES = ['Food', 'Entertainment', 'Car']
    
    expenses = [{
        'category': 'Food',
        'description': 'Hamburgers',
        'amount': 300
    },
    {
        'category': 'Entertainment',
        'description': 'Hamburgers',
        'amount': 300
    },
    {
        'category': 'Car',
        'description': 'Fuel',
        'amount': 300
    }]

    @staticmethod
    def find():
        return Database.expenses

    
    @staticmethod
    def add(expense):
        Database.expenses.append(expense)


    
    