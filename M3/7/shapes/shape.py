from turtle import *
class Shape():
    def __init__(self,border,fill,coordinates,heading):
        self.border = border
        self.fill = fill
        self.coordinates = coordinates
        self.heading = heading

    def draw(self):
        penup()
        goto(self.coordinates[0], self.coordinates[1])
        setheading(self.heading)
        color(self.border,self.fill)
        pendown()
        begin_fill()



    def __str__(self):
        return f'{self.coordinates}  {self.heading} {self.border}  {self.fill}'



