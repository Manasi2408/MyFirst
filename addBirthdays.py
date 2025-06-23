<<<<<<< HEAD
# add friends birthday temporarily for fun

birthdays = {}

while True:
    print("Enter name : (press quit to exit)")
    name = input().upper()

    if name == "QUIT":
        break

    if name in birthdays:
        print(birthdays[name],",",name)
    else:
        print("I do not have the info of this")
        print("When is their birthday?")
        bday = input().upper()

        birthdays[name] = bday

        print("Info updated")
        print()
        print("----------------------------------------------------------------------------------------------")
        for name, date in birthdays.items():
            print("NAME :",name,"\nDATE :",date,"\n")
        print("----------------------------------------------------------------------------------------------")
=======
# add friends birthday temporarily for fun

birthdays = {}

while True:
    print("Enter name : (press quit to exit)")
    name = input().upper()

    if name == "QUIT":
        break

    if name in birthdays:
        print(birthdays[name],",",name)
    else:
        print("I do not have the info of this")
        print("When is their birthday?")
        bday = input().upper()

        birthdays[name] = bday

        print("Info updated")
        print()
        print("----------------------------------------------------------------------------------------------")
        for name, date in birthdays.items():
            print("NAME :",name,"\nDATE :",date,"\n")
        print("----------------------------------------------------------------------------------------------")
>>>>>>> 598ff5df94d24dcf39cb65ec7081fdcd9cb83904
        print()