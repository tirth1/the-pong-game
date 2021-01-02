from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from screen_divider import ScreenDivider

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)
screen.listen()

screen_divider = ScreenDivider()

paddle1 = Paddle("left")
paddle2 = Paddle("right")
ball = Ball()
scoreboard1 = Scoreboard("left")
scoreboard2 = Scoreboard("right")

screen.update()

screen.onkeypress(fun=paddle1.move_up, key="Up")
screen.onkeypress(fun=paddle1.move_down, key="Down")
screen.onkeypress(fun=paddle2.move_up, key="w")
screen.onkeypress(fun=paddle2.move_down, key="s")

game_on = True
while game_on:
    screen.update()
    scoreboard1.score(paddle1.score)
    scoreboard2.score(paddle2.score)
    time.sleep(0.1)
    ball.move()

    # Detect collision with paddle1
    if paddle1.distance(ball) < 50:
        print("paddle1")
        ball.bounce_hor()

    # Detect collision with paddle2
    if paddle2.distance(ball) < 50:
        print("paddle2")
        ball.bounce_hor()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ver()

    # Detect collision with right side wall
    if ball.xcor() > 390:
        paddle1.goal()
        ball.bounce_hor()

    # Detect collision with left side wall
    if ball.xcor() < -390:
        paddle2.goal()
        ball.bounce_hor()

screen.exitonclick()