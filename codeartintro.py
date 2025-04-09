# ### SETUP ###
import turtle

t = turtle.Turtle()
t.penup()
t.goto(-300, -100)
t.color("purple")
t.pendown()

for i in range(2):
    for i in range(3):
        t.forward(40)
        t.left(120)
    t.penup()
    t.right(120)
    t.pendown()
t.backward(40)
t.right(120)
for i in range(3):
        t.forward(40)
        t.left(120)
# ### ENDING ###
turtle.exitonclick()
