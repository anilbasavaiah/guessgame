import random

random_secret = random.randint(1, 1000)


def guessnum(num):
    if num == random_secret:
        print("You guessed the number!!!")
        return True
    elif num < random_secret:
        print("It is too low, try higher number")
    else:
        print("It is too high, try a lower number")


actual_guess = 0

try:
    while guessnum(int(input("Guess the number 1 - 1000: "))) is not True:
        actual_guess += 1
        if actual_guess == 10:
            print(f"You have exceeded the guess limit exiting the game, the correct number was: {random_secret}")
            break
except ValueError as e:
    print("Please enter a valid number, exiting the game")





