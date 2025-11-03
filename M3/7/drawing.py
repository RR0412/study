from shapes import *
from turtle import *
class Drawing():
    def __init__(self):
        self.shapes = [
            Rectangle('black', 'blue', [-100, 0], 0, 200, 50),
            Square('black', 'lightblue', [-50, 50], 0, 50),
            Circle('black', 'black', [-70, -50], 0, 25),
            Circle('black', 'black', [70, -50], 0, 25)
        ]

    def draw(self):
        for shape in self.shapes:
            print(shape)
            shape.draw()
        done()

if __name__ == "__main__":
    drawing = Drawing()
    drawing.draw()