from turtle import Turtle

y = 0
max_y = 300
min_y = -300


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")

    def up(self):
        if y != max_y:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if y != min_y:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
