from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from border import Border
import time

X_RIGHT_PUDDLE = 460
X_LEFT_PUDDLE = -470

game_is_on = True

screen = Screen()
screen.setup(width=1000, height=700)
screen.colormode(255)
screen.bgcolor(53, 56, 61)
screen.title('Pong game')
screen.tracer(0)
screen.listen()

right_paddle = Paddle(X_RIGHT_PUDDLE)
left_paddle = Paddle(X_LEFT_PUDDLE)
border = Border().paint_border()

score_right = Score(75,250)
score_right.write_point()
score_left = Score(-75,250)
score_left .write_point()
ball = Ball()

screen.onkey(key='Up', fun=right_paddle.move_paddle_up)
screen.onkey(key='Down', fun=right_paddle.move_paddle_down)
screen.onkey(key='w', fun=left_paddle.move_paddle_up)
screen.onkey(key='s', fun=left_paddle.move_paddle_down)

while game_is_on:
    screen.update()
    time.sleep(ball.speed_ball)
    ball.move_ball()
    # detect top or bottom
    if ball.ycor() > 330 or ball.ycor() < -320:
        ball.bounce_y()
    # detect right_paddle or left_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 435 or ball.distance(left_paddle) < 50 and ball.xcor() < -445:
        ball.bounce_x()
    # check left and right sides
    if ball.xcor() > 500:
        score_left.points += 1
        ball.reset_position()
        score_left.write_point()
    elif ball.xcor() < -500:
        score_right.points += 1
        ball.reset_position()
        score_right.write_point()
    if score_left.points >= 5 or score_right.points >= 5:
        game_over = Score(0, 0)
        game_over.game_over()
        game_is_on = False

screen.exitonclick()