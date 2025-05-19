# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
s1 = create_sprite("semiminibasket",0,-200)
s2 = create_sprite("minibratapple", 0, 250)
s3 = create_sprite("minibratapple", 0, 250)
score = 0

set_background("apple")
# Section 3: Controls
# TODO - define your controls

    
def move_left():
	s1.setheading(180)
	s1.forward(10)
    
def move_right():    
	s1.setheading(0)
	s1.forward(10)


window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
# TODO - pick keys for each control

# Section 4: Game Loop
window.listen()

s2.goto(random.randint(-250, 250), 250)
while True:
	time.sleep(0.1)	
	# for i in range(10):
	s2.setheading(270)
	s2.forward(10)
	if s2.ycor()<-200:
		s2.goto(random.randint(-250, 250), 250)

		# time.sleep(0.1)
    
 	# TODO - code for automatic actions






	window.update()


	#if s2.ycor()<-250:
		#break
	#elif s3.ycor()<-250:
		#break
	

print("Game Over")
