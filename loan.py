# Eligible to get a loan

while True:
    print("Do you want loan? (yes/no)")
    answer = input().upper()

    if answer == "YES":
        print("How much is your salary annually?")
        try:
            salary = int(input())
        except ValueError:
            print("Enter a valid number.")
            continue

        if 1000000 <= salary <= 2000000:
            print("What is your credit score?")
            try:
                credit = int(input())
            except ValueError:
                print("Enter a valid number.")
                continue

            if 650 <= credit <= 900:
                decision = "approved"
                break    
            elif 300 < credit < 649:
                decision = "denied"
                break
            else:
                print("Credit score out of range.")
                continue

        elif 100000 < salary < 900000:
            credit = "Not applicable"
            decision = "low_income"
            break
        else:
            print("Salary is not in eligible range.")
            continue

    elif answer == "NO":
        print("No worries.")
        salary = 0
        credit = 0
        decision = "exit"
        break

    else:
        print("Error: Please enter yes or no.")
        continue

print()
print("-------- Information --------")
if decision == "approved":
    print("Salary       - ₹", salary, "(High income)")
    print("Credit Score -", credit, "(Good credit score)")
    print("You are eligible to get a loan!")

elif decision == "denied":
    print("Salary       - ₹", salary, "(High income)")
    print("Credit Score -", credit, "(Bad credit score)")
    print("You are not eligible to get a loan.")

elif decision == "low_income":
    print("Salary       - ₹", salary, "(Low income)")
    print("Credit Score -", credit)
    print("You are not eligible to get a loan.")

else:
    print("Program exited.")
