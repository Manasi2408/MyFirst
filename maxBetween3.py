print("Enter 3 number : ")

a = int(input("First : "))
b = int(input("Second : "))
c = int(input("Third : "))

if a > b:
    if a > c:
        print(a,"is the largest")
    else:
        print(c,"is the largest")
else:
    if b > c:
        print(b,"is the largest")
    else:
        print(c,"is the largest")