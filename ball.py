from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color(18, 219, 175)
        self.x_move = 10
        self.y_move = 10
        self.speed_ball = 0.05

    def move_ball (self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y (self):
        self.y_move *= -1
        self.speed_ball *= 0.9

    def bounce_x (self):
        self.x_move *= -1
        self.speed_ball *= 0.99

    def reset_position (self):
        self.goto(0,0)
        self.bounce_x()