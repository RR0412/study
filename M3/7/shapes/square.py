from turtle import *
from .shape import Shape
class Square(Shape):
    def __init__(self,border,fill,coordinates,heading,side):
        super().__init__(border,fill,coordinates,heading)
        self.side = side

    def draw(self):
        super().draw()
        for i in range(4):
            forward(self.side)
            right(90)
        end_fill()



    def __str__(self):
        return super().__str__() + f'Square with a side {self.side}'


# square = Square('blue','green',[-50,-50],90,75)
#
# square.draw()