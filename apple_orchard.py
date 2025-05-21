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
timer = 0

set_background("apple")
# Section 3: Controls
# TODO - define your controls
speed = 0
slow = 0
#fix the timer using a variable
def speedy():
	global speed, timer_fast, timer
	speed += 1
	timer_fast = timer
	s1.write("fast", font = ("Arial", 40, "normal"))
	

def sabotage():

	global slow, timer_slow, timer
	slow += 1 
	timer_slow = timer
	s1.write("slow", font = ("Arial", 40, "normal"))
	



def move_left():
	global speed, slow
	s1.setheading(180)
	if speed <= 0 and slow <= 0 :
		s1.forward(15)
	elif speed > 0:
		s1.forward(25)
	elif slow > 0:
		s1.forward(7)

    
def move_right(): 
	global speed, slow   
	s1.setheading(0)
	if speed <= 0 and slow <=0 :
		s1.forward(15)
	elif speed > 0:
		s1.forward(25)
	elif slow > 0:
		s1.forward(7)

window.onkeypress(speedy, "Up")
window.onkeypress(sabotage, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
# TODO - pick keys for each control

# Section 4: Game Loop
window.listen()

s2.goto(random.randint(-250, 250), 250)
s3.goto(random.randint(-250, 250), 250)
timer_slow = 0
timer_fast = 0
while True:
	time.sleep(0.1)	
	timer += 0.1

	s2.setheading(270)
	s2.forward(10)
	if get_distance(s1,s2)< 70:
		s2.goto(random.randint(-250, 250), 250)
	
	if timer >= 2.4:
		s3.setheading(270)
		s3.forward(10)
		if get_distance(s1,s3)< 70:
			s3.goto(random.randint(-250, 250), 250)
    
 	# TODO - code for automatic actions

	if timer == timer_slow + 30:
		slow = 0
		s1.clear()

	if timer == timer_fast + 30:
		speed = 0
		s1.clear()

	window.update()


	#if s2.ycor()<-250:
		#break
	#elif s3.ycor()<-250:
		#break
	

print("Game Over")
