

from turtle import *
import random

my_screen = Screen()
my_screen.setup(width=500,height=400)

print("Choose a color amongst - pink , blue , green , yellow , purple.")

user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["pink", "blue", "green", "yellow", "purple"]
y_position = [100, 50, 0, -50, -100]
all_turtles = []

for i in range(0, 5):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_position[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Your turtle won! The {winning_color} turtle is the winner!")

            else:
                print(f"Your turtle lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



my_screen.exitonclick()
