import random
import time
import turtle
from turtle import Screen, Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.shape("turtle")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_to_start(self):
        self.goto(0, -230)

    def is_it_finish_line(self):
        if self.ycor() > 240:
            return True
        else:
            return False


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-200, 200)
            new_car.goto(230, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car_elem in self.all_cars:
            car_elem.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


class Table(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 230)
        self.hideturtle()
        self.level = 0
        self.update_score()

    def end_game(self):
        self.goto(-60, 0)
        self.write("Game over", font=("Arial", 20, "normal"))

    def update_score(self):
        self.goto(-220, 230)
        self.color("black")
        self.write(f"Level {self.level}", align="center", font=("Arial", 10, "normal"))

    def level_point(self):
        self.level += 1
        self.clear()
        self.update_score()


screen = Screen()
screen.setup(width=500, height=500)
screen.tracer(0)
car = CarManager()
table = Table()

player = Player()
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

game_is_on = True
n = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    table.update_score()
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            table.end_game()
            game_is_on = False

    if player.is_it_finish_line():
        player.go_to_start()
        car.level_up()
        table.level_point()

screen.exitonclick()
