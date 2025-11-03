from turtle import *
from .shape import Shape
class Circle(Shape):
    def __init__(self,border,fill,coordinates,heading,radius):
        super().__init__(border,fill,coordinates,heading)
        self.radius = radius

    def draw(self):
        super().draw()
        circle(self.radius)
        end_fill()

    def __str__(self):
        return super().__str__() + f'This circle has radius of {self.radius}'


# circle = Circle('blue','yellow',[50,-50],90,100)
# circle.draw()