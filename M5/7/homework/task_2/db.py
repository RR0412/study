class Database:
    counter = 2
    tasks = [{
        'id': 1,
        'title': 'Make up bed',
        'description': 'Tidy up bed',
        'created_at': '12.12.2012 12:12'
    }, {
        'id': 2,
        'title': 'Cook breakfast',
        'description': 'Check the fridge, off you go',
        'created_at': '11.11.2011 11:11'
    }]

    @staticmethod
    def find():
        return Database.tasks

    @staticmethod
    def add(task):
        Database.tasks.append(task)

    @staticmethod
    def find_by_id(id):
        for task in Database.tasks:
            if task['id'] == id:
                return task
        else:
            return None
