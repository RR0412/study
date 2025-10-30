from datetime import datetime

class Clock():
    def show_time(self):
        print(datetime.now().strftime('%H:%M:%S'))

class Calculator():
    def add(self, a, b):
        return a+b

class Camera():
    def take_shot(self):
        print('Bling!')

class SmartPhone(Camera, Clock, Calculator):
    def ring(self):
        print('Na-na-na-na, na-na-na-na,na-na-na-na!')

nokia = SmartPhone()

# nokia.show_time()
# print(nokia.add(1000, 2000))
# nokia.take_shot()
# nokia.ring()

#=============================================================
class FirstParent():
    def where(self):
        print('In first parent')

class SecondParent():
    def where(self):
        print('In second parent')

class Child(FirstParent, SecondParent):
    pass

child = Child()
# child.where()
# =============================================================
class Item():
    def __init__(self):
        self.public_value = 10
        self._protected_value = 20

    def public_method(self):
        print('Public')

    def _protected_method(self):
        print('Protected')

# item = Item()
# print(item.public_value)
# print(item._protected_value)
# item.public_method()
# item._protected_method()

class Parent():
    def __init__(self):
        self.__private_value = 30

    def __private_method(self):
        print('Private')

# item = Parent()

# print(item.__private_value)
# item.__private_method()
#
# print(item._Parent__private_value)
# item._Parent__private_method()


# class Child(Parent):
#     def call_private_method(self):
#         self.__private_method()
#
#     def get_private_value(self):
#         return self.__private_value

# item = Child()
# print(item.get_private_value())
# item.call_private_method()

# class Child(Parent):
#     def call_private_method(self):
#         self._Parent__private_method()

#     def get_private_value(self):
#         return self._Parent__private_value

# item = Child()
# print(item.get_private_value())
# item.call_private_method()
# =============================================================
# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if 0 <= age <= 120:
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
#
#     def  get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         self._name = name

# person = Person("Alice", 30)
# print(person.get_age())
# person.set_age(100)
# print(person.get_age())
# person.get_age()
# person.set_age(50)
# =============================================================
class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 <= age <= 120:
            self.__age = age

        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

person = Person("Alice", 30)
print(person.age)
print(person.name)
person.age = 35
print(person.age)
person.age = 150


