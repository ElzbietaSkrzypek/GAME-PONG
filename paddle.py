from turtle import Turtle

POSITION = [(370, 0), (-370, 0)]
UP = 90


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 4)
        self.penup()
        self.setheading(UP)
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)