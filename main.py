from turtle import Turtle, Screen
import random

# Setting up screen parameters
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")

# Betting input and setting turtle positions
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# for loop to create 6 different turtles and appending them to all_turtles list
all_turtles = []
is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

# Start a while loop and giving each turtle a random "speed"
while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0,6)
        turtle.forward(random_distance)
        # if statement to determine the winning turtle after xcor > 230
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost. The {winning_color} is the winner!")

screen.exitonclick()

