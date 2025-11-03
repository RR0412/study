from turtle import *
from .shape import Shape
class Triangle(Shape):
    def __init__(self,border,fill,coordinates,heading,side):
        super().__init__(border,fill,coordinates,heading)
        self.side = side

    def draw(self):
        super().draw()
        begin_fill()
        forward(self.side)
        right(90)
        forward(self.side)
        right(135)
        forward(self.side)
        end_fill()
        penup()
        home()
        pendown()


    def str(self):
        return super().__str__() + f'This triangle have side {self.side} long '

# triangle = Triangle('pink','black',[-50,50],45,50)
# triangle.draw()