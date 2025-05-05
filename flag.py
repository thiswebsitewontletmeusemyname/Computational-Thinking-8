import turtle
t = turtle.Turtle()

# setup
t.speed(10)
turtle.Screen().bgcolor("light blue")
width = 60
length = 100
denmark = 8
# stripes

# move to stripe 1
t.goto(-50, -20)

# stripe 1
t.color("red")
t.begin_fill()
t.forward(length)
t.left(90)
t.forward(width)
t.left(90)
t.forward(length)
t.left(90)
t.forward(width)
t.left(90)
t.end_fill()
t.penup()
t.goto(-40, -20)
t.color("white")
t.begin_fill()
t.pendown()
t.forward(denmark)
t.left(90)
t.forward(width)
t.left(90)
t.forward(denmark)
t.left(90)
t.forward(width)
t.left(90)
t.end_fill()

t.penup()

t.goto(-50, 10)
t.color("white")

t.begin_fill()
t.pendown()

t.forward(length)
t.left(90)
t.forward(denmark)
t.left(90)
t.forward(length)
t.left(90)
t.forward(denmark)
t.left(90)
t.end_fill()

turtle.exitonclick()
