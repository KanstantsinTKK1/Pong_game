from turtle import Turtle
START_LINE = -350

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, START_LINE)
        self.shape('square')
        self.shapesize(5,0.2)
        self.line_position = 0
        self.pensize(5)

    def paint_border(self):
        for num in range(12):
            self.line_position += 47
            self.pendown()
            self.goto(0, START_LINE + self.line_position)
            self.line_position += 47
            self.penup()
            self.goto(0, START_LINE + self.line_position)

