# age and voting 

age = int(input("Enter age : "))
if age >= 18:
    print("Valid to Vote")
elif age <= 0:
    print("Error")
else:
    print("You are a minor")