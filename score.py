from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 75, 'normal')
FONT_GAME_OVER = ('Courier', 40, 'normal')

class Score(Turtle):
    def __init__(self,x_position, y_position):
        super().__init__()
        self.ht()
        self.penup()
        self.color('white')
        self.goto(x_position,y_position)
        self.points = 0

    def write_point(self):
        self.clear()
        self.write(f'{self.points}', move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.write(f'Game Over', move=False, align=ALIGN, font=FONT_GAME_OVER)