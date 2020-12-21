from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
speeds = [0, 10, 6, 3, 1]
all_turtles = []
y = -190
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:? ").lower()

for color in colors:
    turtle_color = color
    new_turtle = Turtle("turtle")
    new_turtle.color(turtle_color)
    new_turtle.penup()
    for a in range(0, 6):
        y += 10
        new_turtle.goto(-230, y)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost The {winning_color} turtle is the winner")
        turtle.speed(random.choice(speeds))
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
