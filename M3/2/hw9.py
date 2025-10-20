1
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



rectangle = Rectangle(10,20)
print(rectangle.square())
print(rectangle.perimeter())
print(rectangle.parameters())





