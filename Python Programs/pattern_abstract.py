import turtle
#neeraja
tut = turtle.Screen()
tut.bgcolor("White")
pen = turtle.Turtle()
#speed of pen
pen.speed(500)
pen.color("Pink")
pen.width(10)
tut = turtle.Screen()
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(130)
for x in range(180):
    pen.backward(1)
    pen.right(1)
pen.right(90)
pen.forward(50)
pen.left(90)
for x in range(180):
    pen.backward(1)
    pen.right(1)

pen.right(90)
pen.forward(130)
pen.right(90)
pen.forward(130)
pen.right(90)
pen.forward(130)
for x in range(180):
    pen.backward(1)
    pen.right(1)
pen.right(90)
pen.forward(130)
turtle.done()