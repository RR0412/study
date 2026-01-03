class Database:
    MARKS = ["Mercedes Benz", "Toyota", "BMW", "Subaru"]
    COUNTER = 1
    ads = [{
    "id": 1,
    "mark": "Mercedes Benz",
    "year": 2002,
    "price": 6000,
    "image": "https://upload.wikimedia.org/wikipedia/commons/a/aa/2002_Mercedes-Benz_E240_%28front%29.jpg",
    "description": "C230 Sports Coupe, a car designed to attract first-time Mercedes buyers with its combination of style, space, and a very complete equipment package",
    "contacts": "Please contact by email sale@carsale.com or phone 555 555 555"
    },
]

    @staticmethod
    def find():
        return Database.ads
    
    @staticmethod
    def add(ad):
        Database.ads.append(ad)

    @staticmethod
    def find_by_id(id):
        for ad in Database.ads:
            if ad['id'] == id:
                return ad
        else:
            return None