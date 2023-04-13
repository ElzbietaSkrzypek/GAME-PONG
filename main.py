from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
ALIGNMENT = "center"
FONT = ('Courier', 50, 'normal')

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

dashed_line = Turtle()
dashed_line.goto(0, -400)
dashed_line.color("white")
dashed_line.setheading(90)
for _ in range(600):
    dashed_line.forward(20)
    dashed_line.penup()
    dashed_line.forward(20)
    dashed_line.pendown()

paddle1 = Paddle((370, 0))
paddle2 = Paddle((-370, 0))
ball = Ball()
paddle1_score = Scoreboard()
paddle1_score.score((50, 200))
paddle2_score = Scoreboard()
paddle2_score.score((-50, 200))

# Input Players names
name_1 = screen.textinput(title="Players names", prompt="Player1: ")
name_2 = screen.textinput(title="Players names", prompt="Player2: ")

screen.listen()
screen.onkeypress(paddle1.go_up, "Up")
screen.onkeypress(paddle1.go_down, "Down")
screen.onkeypress(paddle2.go_up, "w")
screen.onkeypress(paddle2.go_down, "s")

game_is_on = False

if name_1 and name_2:
    game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall:

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with paddle1

    if ball.distance(paddle1) < 45 and ball.xcor() > 350:
        ball.hit()
        ball.move_speed *= 0.9

    # Detect collision with paddle2

    if ball.distance(paddle2) < 45 and ball.xcor() < -350:
        ball.hit()
        ball.move_speed *= 0.9

    # Detect missing the ball and update the scoreboard

    if ball.xcor() > 370:
        ball.home()
        ball.bounce()
        ball.hit()
        paddle2_score.increase_score()
        paddle2_score.score((-50, 200))
    if ball.xcor() < -370:
        ball.home()
        ball.bounce()
        ball.hit()
        paddle1_score.increase_score()
        paddle1_score.score((50, 200))

    # Game Over

    if paddle1_score.point == 10 or paddle2_score.point == 10:
        if paddle1_score.point == 10:
            winner = name_1
        else:
            winner = name_2
        game_is_on = False
        ball.hideturtle()
        ball.goto(0, 0)
        ball.hideturtle()
        ball.write(f"{winner} won!", align=ALIGNMENT, font=FONT)



screen.update()
screen.exitonclick()
