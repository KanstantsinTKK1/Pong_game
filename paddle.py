from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.pencolor('blanched almond')
        self.fillcolor('blanched almond')
        self.shape('square')
        self.shapesize(5, 1, 2)
        self.goto(x_position, 0)


    def move_paddle_up(self):
        current_y = self.ycor()
        new_y = current_y + 20
        self.goto(self.xcor(), new_y)

    def move_paddle_down(self):
        current_y = self.ycor()
        new_y = current_y - 20
        self.goto(self.xcor(), new_y)
