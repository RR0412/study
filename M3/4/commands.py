from datetime import datetime
class Dog:
    def __init__(self,name):
        self.name = name

    def bark(self):
        print('Woof')


class Chihuahua(Dog):
    def bark(self):
        print('Yip')

little_dog = Chihuahua('Fluffy')
little_dog.bark()
little_dog = Chihuahua('Chappy')
print(little_dog.name)
little_dog.bark()

class Bulldog(Dog):
    def growl(self):
        print('Grrrr!')

big_dog = Bulldog('Terry')
big_dog.growl()
big_dog.bark()


class Log:
    def __init__(self):
        self.entries = []

    def write(self,text):
        self.entries.append(text)

    def read(self):
        for text in self.entries:
            print(text)

class TimeLog(Log):
    def write(self,text):
        self.entries.append('%s' % datetime.now())
        super().write(text)

log = TimeLog()
log.write('First entry')
log.write('Other entry')
log.read()

class Log:
    PARAGRAPH_INDENT = '      '

    def __init__(self):
        self.entries = []

    def write(self,text):
        formatted_text = text.strip().capitalize()
        entry = f'{self.PARAGRAPH_INDENT} {formatted_text} \n'
        self.entries.append(entry)

    def read(self):
        for text in self.entries:
            print(text)


class TimeLog(Log):
    def write(self,text):
        self.entries.append(f'{datetime.now()}')
        super().write(text)

log = TimeLog()
log.write('First entry')
log.write('Other entry')
log.read()


class TalkingDog(Dog):
    def __str__(self):
        return f'I am talking dog. My name is {self.name}'

talking_dog = TalkingDog('Ivory')

dog_as_string = str(talking_dog)
print(dog_as_string)

