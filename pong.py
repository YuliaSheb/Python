import time
from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def refresh(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)
        time.sleep(0.1)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()


class Table(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.score1, align="center", font=("Arial", 28, "normal"))
        self.goto(100, 200)
        self.write(self.score2, align="center", font=("Arial", 28, "normal"))

    def score1_point(self):
        self.score1 += 1
        self.clear()
        self.update_score()

    def score2_point(self):
        self.score2 += 1
        self.clear()
        self.update_score()


screen = Screen()
screen.setup(width=700, height=500)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

paddle1 = Paddle((320, 0))
paddle2 = Paddle((-320, 0))
ball = Ball()
k = ["slowest", "slow", "normal", "fast", "fastest"]
ball.speed(k[0])
table = Table()
i = 0

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.refresh()
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_y()
    if ball.distance(paddle1) < 50 and ball.xcor() > 240 or ball.distance(paddle2) < 50 \
            and ball.xcor() < -240:
        ball.bounce_x()
        if i in k:
            ball.speed(k[i])
            i += 1
        else:
            ball.speed(k[-1])

    if ball.xcor() > 350:
        ball.reset_position()
        table.score1_point()
    if ball.xcor() < -350:
        ball.reset_position()
        table.score2_point()

screen.exitonclick()
