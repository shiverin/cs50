import random
while True:
    try:
        x = int(input("Level: "))
        if x <= 0:
            continue
        break
    except ValueError:
        pass

y = random.randint(0, x)
while True:
    try:
        x = int(input("Guess: "))
        if x < y:
            print("Too small!")
        elif x > y:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
