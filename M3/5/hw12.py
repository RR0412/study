class BankAccount:
    def __init__(self,__balance,__account_number,_owner):
        self.__balance = __balance
        self.__account_number = __account_number
        self._owner = _owner

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if self.__balance < amount:
            print('Insufficient funds')
        else:
            self.__balance -= amount

    def account_info(self):
        return f'Balance : {self.__balance}  \nAccount Number : {self.__account_number}  \nOwner : {self._owner}'

    @property
    def owner(self):
        return self._owner


    @owner.setter
    def owner(self,owner):
        for char in owner:
            if char.isdigit():
                print('No numbers allowed')
                break
        else:
            self._owner = owner


    @property
    def get_balance(self):
        return self.__balance

    @property
    def get_account_number(self):
        return self.__account_number

client_1 = BankAccount(10000,123456,"Marcus")
client_1.__balance = 50000
print(client_1.get_balance)
client_1.__account_number = 888888
print(client_1.get_account_number)
client_1.deposit(50000)
print(client_1.get_balance)
client_1.withdraw(30000)
print(client_1.get_balance)
client_1._owner = 'Anthony'
print(client_1.owner)
print(client_1.account_info())
