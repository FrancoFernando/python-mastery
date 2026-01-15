import random

def guessing_game():

    left, right = 0, 100
    integer = random.randint(0,100)
    while True:
        guess = int(input(f"Which is the next number to guess [{left}-{right}]: "))

        if guess < left or guess > right:
            continue

        if guess < integer:
            left = guess
            print("too low")
        elif guess > integer:
            print("too high")
            right = guess
        else:
            print(f"You guessed the right number:{guess}")
            break

guessing_game()

