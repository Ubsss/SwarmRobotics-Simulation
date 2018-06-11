import turtle
import os

#Set up the screen
mS = turtle.Screen()
mS.bgcolor('black')
mS.title("First Game")

#Draw border
borderMarker = turtle.Turtle()
borderMarker.speed(0)
borderMarker.pencolor("Red")
borderMarker.penup()
borderMarker.setposition(-300,-300)
borderMarker.pendown()

for side in range(4):
    borderMarker.fd(600)
    borderMarker.lt(90)
borderMarker.hideturtle()











#Delay the screen closing
turtle.exitonclick()

#delay = raw_input("Press enter to finish... ")