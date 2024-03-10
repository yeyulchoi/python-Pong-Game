from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(ball.move,"m")

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    #collide with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
   # collide with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.right_point()

























screen.exitonclick()