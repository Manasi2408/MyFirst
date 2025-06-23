# number search

number = []

print("Enter numbers :")

while True:
    print("Number",len(number)+1,":")
    i = input()

    if i == "":
        break
    
    try:
        number.append(int(i))
    except ValueError:
        print("Please enter a number ")
        continue

if not number:
    print("No numbers were entered")
else:
    print("The numbers entered are :")
    for i in number:
        print(i)

    print("Enter a number you want to search in this list : ")
    search = int(input())

    if search in number:
        print("Yes",search,"is present")
    else:
        print(search,"is not present")