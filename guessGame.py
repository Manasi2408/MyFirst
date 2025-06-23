# make a guessing number game

import random

secretNumber = random.randint(1,20)

print("I am thinking of a number between 1 to 20")
print("You have only 5 chances")

for i in range(1,6):
    print("Take a guess : ")
    guess = int(input())

    if guess > secretNumber:
        print("Your guess is too high.")
    elif guess < secretNumber:
        print("Your guess is too low.")
    else:
        break

if guess == secretNumber:
    print("Yes! You have guessed the number right in",i,"chances")
else:
    print("Nope. I was thinking of",secretNumber)