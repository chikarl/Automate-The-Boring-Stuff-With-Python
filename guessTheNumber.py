from math import ceil, floor
from random import random


print("I am thinking of a number between 1 and 10")
cp_number = ceil(random()*10)
for i in range(6):
    user_number = int(input("Take a guess: "))
    if user_number == cp_number:
        print(f"Good job! You guessed my number in {i+1} guesses")
        break
    elif user_number > cp_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
