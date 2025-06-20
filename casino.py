# casino game

import random

name = "xyz"
password = "123xyz"
balance = 10000
total = balance


while True:
    print("Enter your name :")
    userName = input()

    if userName != name:
        print("Bruh !")
        continue

    print("Enter password :")
    userPass = input()

    if userPass != password:
        print("Oh God !")
        continue

    print("-----------------------------------------------------------------------------------------------------")
    print("Welcome to Casino Night, your balance is :",balance)
    break


while True:
        if balance < 500:
            print("Insufficient Balance")
            break
        
        print("-----------------------------------------------------------------------------------------------------")
        print("To play the game, you have to invest 500")
        print("If you win, you get the 1000 or if you lose you lose")
        print("Type 'play' to continue or 'quit' to stop")
        answer = input().lower()

        if answer == "play":
            print("Enter a number (1-10):")
            try:
                number = int(input())
            except ValueError:
                print("Number you idiot !")
                continue
    
            ranum = random.randint(1,10)
            print("Casino number was:",ranum)
                
            if number == ranum:
                    print("You won 500")
                    total += 1000
                    print("Your balance is:",total)
            else:
                    print("You lost 500")
                    total -= 500
                    print("Your balance is :",total)
        elif answer == "quit":
            print("Scardy Cat !")
            break
        else:
             print("Stop messing")