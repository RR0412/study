from turtle import *
from .shape import Shape
class Rectangle(Shape):
    def __init__(self,border,fill,coordinates,heading,width,height):
        super().__init__(border,fill,coordinates,heading)
        self.width = width
        self.height = height


    def draw(self):
        super().draw()
        for i in range(2):
            forward(self.width)
            right(90)
            forward(self.height)
            right(90)
        end_fill()



    def __str__(self):
        return super().__str__() + f'Rectangle {self.height} x {self.width}'


# rectangle = Rectangle('yellow','red',[50,50],90,50,100)
#
# rectangle.draw()