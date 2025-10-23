#1
class  Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def perimeter(self):
        perimeter = 2*(self.width + self.height)
        return perimeter

    def square(self):
        square = self.width * self.height
        return square

    def parameters(self):
        parameters = (f'The width of rectangle is {self.width},\n'
              f'The height of rectangle is {self.height},\n'
              f'The perimeter of rectangle  is {self.perimeter()},\n'
              f'The square of rectangle  is {self.square()}')
        return parameters


#2
class Book:
    def __init__(self, title, author=None, year=None):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        if self.author and self.year:
            info = f'\n{self.title:<30} {self.author:^20} {self.year:>5}'
        elif self.author:
            info = f'\n{self.title:<30} {self.author:^20} {"":>5}'
        elif self.year:
            info = f'\n{self.title:<30} {"":^20} {self.year:>5}'
        return info
#3
class Library:
    def __init__(self, name):
        self.name = name
        self.book_list = []

    def list(self):
        spisok = f'{"Название":<30} {"Автор":^20} {"Год":>5}'
        for book in self.book_list:
            spisok += book.display()
        return spisok

    def filter(self, title=None, author=None, year=None):
        result = []
        for book in self.book_list:
            if title and (book.title is None or book.title.lower() != title.lower()):
                continue
            if author and (book.author is None or book.author.lower() != author.lower()):
                continue
            if year and book.year != year:
                continue
            result.append(book)
        return result

    def add_book(self, book):
        self.book_list.append(book)

    def delete_book(self, book):
        self.book_list.remove(book)

    @staticmethod
    def as_table(book_list):
        spisok = f'{"Название":<30} {"Автор":^20} {"Год":>5}\n'
        for book in book_list:
            spisok += book.display()
            spisok += '\n'
        return spisok


book_1 = Book('Чистый код', 'Дядя Боб', 2017)
book_2 = Book('От 2 до 5', 'Корней Чуковский', 1958)
book_3 = Book('Идеальный программист', 'Дядя Боб', 2018)
book_4 = Book('Рецепты татарской кухни' ,year=2018)

library = Library('Домашняя библиотека')
library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.add_book(book_4)

# print(library.name)
# print(library.list())

# books = library.filter(author='Корней Чуковский', title='От 2 до 5')
# print(books[0].display())

books = library.filter(author='Дядя Боб')
Library.as_table(books)









