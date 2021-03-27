from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Turtle Racing Game", prompt="Who's going to win:")
colors = ("red", "orange", "green", "yellow", "blue", "purple")
all_turtles = []

print(user_bet)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=-100 + (turtle_index * 30))
    all_turtles.append(new_turtle)

print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"you've won, the winning turtle is {winning_color}")
            else:
                print(f"you've lost, the winning turtle is {winning_color}")
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()
