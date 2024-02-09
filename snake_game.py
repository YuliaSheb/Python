import random
import time
from turtle import Screen, Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for _ in STARTING_POSITION:
            self.add_segment(_)

    def add_segment(self, position):
        segment = Turtle()
        segment.color("white")
        segment.penup()
        segment.goto(position)
        segment.shape("square")
        self.snake.append(segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(new_x, new_y)
        self.snake[0].forward(20)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-210, 210)
        random_y = random.randint(-210, 210)
        self.goto(random_x, random_y)


class Table(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.hideturtle()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", "w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}     High score: {self.high_score}", align="center", font=("Arial", 12, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def end_game(self):
        self.goto(-60, 0)
        self.color("red")
        self.write("Game over", font=("Arial", 20, "normal"))


screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

tom = Snake()
food = Food()
table = Table()

screen.listen()
screen.onkey(tom.up, "Up")
screen.onkey(tom.down, "Down")
screen.onkey(tom.left, "Left")
screen.onkey(tom.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    tom.move()
    if tom.head.distance(food) < 15:
        table.increase_score()
        food.refresh()
        tom.extend()
    if tom.head.xcor() > 240 or tom.head.xcor() < -240 or tom.head.ycor() > 240 or tom.head.ycor() < -240:
        table.reset()
        tom.reset()
        table.end_game()
        game_is_on = False
    for segment in tom.snake[1:]:
        if tom.head.distance(segment) < 10:
            table.reset()
            tom.reset()
            table.end_game()
            game_is_on = False


screen.exitonclick()
