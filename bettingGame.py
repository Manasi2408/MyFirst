# Betting Game

import random

print("This is a Betting Game !")
print()
print("Enter a number of your choice but the number should match the computer's generated number in order to win the game !")
print("------------------------------------------------------")
print("Enter a number:")
number = input()
print("Your number is:",number)
r = random.randint(1,10)
print("The computer's number is:",r)

if number == r:
    print("You have won the lottery !")
else:
    print("Better luck next time !")