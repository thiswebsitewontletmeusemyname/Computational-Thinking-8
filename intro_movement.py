# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite

window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
set_background("fall")
s1 = create_sprite("corgi",0,-200)
def reset(x,y):
	s1.goto(x,y)
window.onscreenclick(reset)


# Section 3: define movement controls
def move_up():
	s1.setheading(90)
	s1.forward(10)
   	 
def move_down():
	s1.setheading(270)
	s1.forward(10)
    
def move_left():
	s1.setheading(180)
	s1.forward(10)
    
def move_right():    
	s1.setheading(0)
	s1.forward(10)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

# Section 4: define other controls
# hide and show controls
def hide():
	s1.hideturtle()
def show():
	s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

# Section 4.5: draw

def draw():
	s1.pendown()
	
def stop_drawing():
	s1.penup()
	
window.onkeypress(draw, "c")

window.onkeyrelease(stop_drawing, "c")

def erase():
	s1.clear()
window.onkeypress(erase, "v")

def pink():
	s1.color("pink")
window.onkeypress(pink, "p")

def pink():
	s1.color("pink")
window.onkeypress(pink, "p")

def blue():
	s1.color("lightsteelblue")
window.onkeypress(blue, "b")

#new sprite

s2 = create_sprite("fish",0,-200)
def reset(x,y):
	s2.goto(x,y)
window.onscreenclick(reset)


# Section 3: define movement controls
def move_up():
	s2.setheading(90)
	s2.forward(10)
   	 
def move_down():
	s2.setheading(270)
	s2.forward(10)
    
def move_left():
	s2.setheading(180)
	s2.forward(10)
    
def move_right():    
	s2.setheading(0)
	s2.forward(10)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# Section 4: define other controls
# hide and show controls
def hide():
	s2.hideturtle()
def show():
	s2.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

# Section 4.5: draw

def draw():
	s2.pendown()
	
def stop_drawing():
	s2.penup()
	
window.onkeypress(draw, "c")

window.onkeyrelease(stop_drawing, "c")

def erase():
	s2.clear()
window.onkeypress(erase, "v")

def pink():
	s2.color("pink")
window.onkeypress(pink, "p")

def pink():
	s2.color("pink")
window.onkeypress(pink, "p")

def blue():
	s2.color("lightsteelblue")
window.onkeypress(blue, "b")


# Section 5: game loop'
window.listen()
while True:
	time.sleep(0.01)
	window.update()