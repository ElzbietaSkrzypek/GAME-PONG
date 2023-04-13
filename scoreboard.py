from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 50, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = 0

    def score(self, position):
        self.goto(position)
        self.hideturtle()
        self.pencolor("white")
        self.write(f"{self.point}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.point += 1
        self.clear()



