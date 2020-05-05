# Guessing game from 1 - 100
import random

randNum = random.randint(1,100)
print(f"The random # is {randNum}")

guess = int(input("Guess a # between 1 and 100: "))

for i in range(5):
    if guess < randNum:
        print("The number is higher")
    elif guess > randNum:
        print("The number is lower")
    else:
        print("That's right!")
        break
    
    guess = int(input("Guess another # "))