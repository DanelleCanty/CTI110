#Danelle Canty
#07-01-2026
#P4LAB1
#Use turtle and loops to draw a triangle and a square


#Import the library
import turtle

#Create the turtle window and drawing objecr
win = turtle.Screen()
win.bgcolor("lightblue")
pen = turtle.Turtle()


# Set turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")


# For loop that draws the square
for side in range(4):
    pen.forward(200)
    pen.right(90)

# While loop that executes 3 times
sides = 3
while sides > 0:
    pen.forward(200)
    pen.left(120)
    sides = sides - 1

win.mainloop() 