# class Cat:
#     pass
#
# murka = Cat()
# barsik = Cat()
#
# print(type(murka))
# print(type(barsik))
#
#
# class Cat():
#     def meow(self):
#         print('Meow!')
#
#     def purr(self):
#         print('Purr!')
#
#     def ask_food(self):
#         for i in range(3):
#             self.meow()
#         self.purr()
#
#
#
# murka = Cat()
# murka.meow()
#
# class Cat():
#     def __init__(self, name, age=None, color='Tabby Gray'):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.is_sleeping =  False
#
#     def meow(self):
#         if self.is_sleeping:
#             print('...ZzZz')
#         else:
#             print('Meow!')
#
#     def sleep(self):
#         self.is_sleeping = True
#
#     def  wake_up(self):
#         self.is_sleeping =  False
#
# barsik = Cat('Barsik', color='Tabby red')
# print(barsik.name)
# print(barsik.age)
# print(barsik.color)
# barsik.age = 2
# print(barsik.age)
#
# murka = Cat('Murka', color ='Black')
# murka.sleep()
# murka.meow()
# murka.wake_up()
# murka.meow()
#
# class Cat:
#     name = None
#     age = None
#     color =  "Tabby Gray"
#
# print(Cat.name)
# print(Cat.age)
# print(Cat.color)
#
#
# cat = Cat()
# print(cat.color)
#
# cat.name = 'Barsik'
# print(cat.name)
#
# print(Cat.name)
#
# class Cat:
#     def __init__(self, name, age=None, color='Tabby Gray'):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     @classmethod
#     def kitten(cls,parent,name):
#         return cls(name, 0, parent.color)
#
# murka = Cat('Murka', 1, 'Black')
# kitten = Cat.kitten(murka, 'Green-eyes')
#
# print(kitten.name)
# print(kitten.color)
# print(kitten.age)
#
# other_kitten = murka.kitten(murka, 'Red-tail')
# print(other_kitten.name)
# print(other_kitten.color)
# print(other_kitten.age)
#

# def to_camel_case(string):
#         words = string.split('_')
#         capitalized_words = [word.capitalize() for word in words]
#         return ''.join(capitalized_words)
#
#
# def to_snake_case(string):
#     new_string = ''
#     prev_char = ''
#     for char in string:
#         if char.isupper():
#             if prev_char.islower():
#                 new_string += '_'
#             new_string += char.lower()
#         else:
#             new_string += char
#         prev_char = char
#     return new_string
#
# def to_big_snake_case(string):
#     return to_snake_case(string).upper()

# class CaseUtils:
#     @staticmethod
#     def to_camel_case(string):
#         words = string.split('_')
#         capitalized_words = [word.capitalize() for word in words]
#         return ''.join(capitalized_words)
#
#     @staticmethod
#     def to_snake_case(string):
#         new_string = ''
#         prev_char = ''
#         for char in string:
#             if char.isupper():
#                 if prev_char.islower():
#                     new_string += '_'
#                 new_string += char.lower()
#             else:
#                 new_string += char
#             prev_char = char
#         return new_string
#
#     @staticmethod
#     def to_big_snake_case(string):
#         return CaseUtils.to_snake_case(string).upper()
#
#
# case_utils = CaseUtils()
# print(case_utils.to_big_snake_case('CamelToBigSnake'))
#

class Logger:
    LOG_PREFIX = 'my_app_log_'
    LOG_TYPES = ['file', 'console', 'database', 'none']
    # log something here

APP_NAME = 'Python App'

