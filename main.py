from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scorecard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle(-350)
paddle2 = Paddle(350)
ball = Ball()
score = Scorecard()

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collisions with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.rebound_y()

    # Detecting collisions with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() < -320 or ball.distance(paddle2) < 50 and ball.xcor() > 320:
        ball.rebound_x()

    # Detecting when the ball misses the paddle
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick()
