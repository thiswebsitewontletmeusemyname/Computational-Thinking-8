#Beginning
sabrina_points = 0
olivia_points = 0

#Middle
answer = input("do you prefer a) fall/winter, or b) spring/summer?")
if answer == "a":
    olivia_points += 1
elif answer == "b":
    sabrina_points += 1

answer = input("do you prefer a) hearts, or b) stars?")
if answer == "b":
    olivia_points += 1
elif answer == "a":
    sabrina_points += 1

answer = input("do you prefer a) purple + dark red + black, or b) pink + baby blue + pastel yellow?")
if answer == "a":
    olivia_points += 1
elif answer == "b":
    sabrina_points += 1

answer = input("do you prefer a) gracie abrams, or b) conan gray?")
if answer == "b":
    olivia_points += 1
elif answer == "a":
    sabrina_points += 1

answer = input("do you prefer a) sour patch kids, or b) heart-shaped chocolates?")
if answer == "a":
    olivia_points += 1
elif answer == "b":
    sabrina_points += 1

#End
if olivia_points > sabrina_points:
    print("You are more like Olivia Rodrigo!")
elif olivia_points < sabrina_points:
    print("You are more like Sabrina Carpenter!")