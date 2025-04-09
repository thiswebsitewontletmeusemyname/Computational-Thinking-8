# ### SETUP ###
import turtle
turtle.Screen().bgcolor("black")
t = turtle.Turtle()
t.penup()
t.goto(-20, 0)
colors = ["yellow", "orange"]
t.pendown()
#set beginging code
for i in range(5):
    t.color( colors[ i % 2] )
    t.left(45)
    t.forward(40)
    t.right(117)
    t.forward(40)
#draw star
t.penup()
t.right(40)
t.forward(7)
t.left(40)
t.pendown()
#move inside
for i in range(5):
    t.color( colors[ i % 2] )
    t.left(45)
    t.forward(30)
    t.right(117)
    t.forward(30)
t.penup()
t.right(40)
t.forward(7)
t.left(40)
t.pendown()
for i in range(5):
    t.color( colors[ i % 2] )
    t.left(45)
    t.forward(20)
    t.right(117)
    t.forward(20)
t.penup()
t.right(40)
t.forward(7)
t.left(40)
t.pendown()
for i in range(5):
    t.color( colors[ i % 2] )
    t.left(45)
    t.forward(10)
    t.right(117)
    t.forward(10)
t.penup()
t.right(40)
t.forward(4)
t.left(40)
t.pendown()
for i in range(5):
    t.color( colors[ i % 2] )
    t.left(45)
    t.forward(5)
    t.right(117)
    t.forward(5)
# ### ENDING ###
turtle.exitonclick()