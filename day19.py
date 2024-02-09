import random
from turtle import Turtle, Screen


# tim = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.left(180)
#     tim.forward(10)
#
#
# def move_left():
#     tim.left(10)
#     tim.forward(10)
#
#
# def move_right():
#     tim.right(10)
#     tim.forward(10)
#
#
# def clear():
#     tim.clear()
#     tim.home()
#
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(move_left, "a")
# screen.onkey(move_right, "d")
# screen.onkey(clear, "c")
# screen.exitonclick()


colors = ["red", "orange", "yellow", "green", "blue", "purple"]

i = 0
k = 0


def make_turtle(x):
    global i
    global k
    x = Turtle(shape="turtle")
    x.penup()
    x.goto(x=-230, y=-100+k)
    x.color(colors[i])
    i += 1
    k += 50
    return x


screen = Screen()
screen.setup(width=500, height=400)
all_turtle = [make_turtle("timmy"), make_turtle("tommy"), make_turtle("tinny"), make_turtle("tonny"),
              make_turtle("toby"), make_turtle("tiny")]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color : ")
print(user_bet)


end = False


if user_bet:
    end = True


while end:
    for turtles in all_turtle:
        if turtles.xcor() > 230:
            end = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle win!")
            else:
                print(f"You've lost! The {winning_color} turtle win!")
        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)


screen.exitonclick()
