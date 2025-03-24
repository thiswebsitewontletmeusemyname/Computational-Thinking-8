while True:
    word = input("What do you think grandma likes?")

    if len(word) > 5:
        print(f"Grandma likes {word}!")
    else:
        print(f"Grandma doesn't like {word}!")
