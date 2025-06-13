# bank program

balance = 100000
total = balance
name = "Manasi"
password = "123mb"
count = 3

def withdraw():
    global total

    print("How much amount you want to withdraw ?")
    try:
        amountWithdraw = int(input())
    except ValueError:
        print("Please enter a number.")

    if amountWithdraw <= 0:
        print("Amount withdrawal should be postive and not 0.")
    elif amountWithdraw > total:
        print("Insufficient balance.")
    else:
        total -= amountWithdraw
        print("You have withdrawn ₹",amountWithdraw)
        print("You have ₹",total)
    
def deposit():
    global total 

    print("Deposit the amount : ")
    try:
        amountDeposit = int(input())
    except ValueError:
        print("Please enter a number.")
        

    if amountDeposit <= 0:
        print("Amount deposited should be positive.")
    else:
        total = total + amountDeposit
        print("You have ₹",total,"total")

print("Welcome to the Bank")

loggedIn = False
while count > 0:
    print("Enter name.",count,"attempts left.")
    userName = input()

    if userName != name:
        print("Invalid name!")
        count -= 1
        continue

    print("First access granted. Enter password :")
    userPassword = input()

    if userPassword != password:
        print("Invalid Password.")
        count -= 1
        continue
    else:
        print("Access granted.")
        loggedIn = True
        break

if not loggedIn:
    print("Too many wrong attempts. Access denied.")
    print("End of program.")
    exit()


while True:
    print("Do you want to withdraw or deposit or quit ?")
    answer = input().upper()

    if answer == "WITHDRAW":
        withdraw()
    elif answer == "DEPOSIT":
        deposit()
    elif answer == "QUIT":
        break
    else:
        print("Invalid option. Please type 'withdraw', 'deposit', or 'quit'.")

print("End of program")