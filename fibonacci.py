<<<<<<< HEAD
# fibonacci series 

a = 0
b = 1
sum = 0

print("Fibonacci series :")

print("Enter number of series you want :")
try:
    series = int(input())
    if series <= 0:
        print("Enter a positive number")
    else:
        print(a,b, end = " ")

        for i in range(2,series):
            sum = a + b
            a = b
            b = sum
            print(sum,end = " ")

except ValueError:
=======
# fibonacci series 

a = 0
b = 1
sum = 0

print("Fibonacci series :")

print("Enter number of series you want :")
try:
    series = int(input())
    if series <= 0:
        print("Enter a positive number")
    else:
        print(a,b, end = " ")

        for i in range(2,series):
            sum = a + b
            a = b
            b = sum
            print(sum,end = " ")

except ValueError:
>>>>>>> 598ff5df94d24dcf39cb65ec7081fdcd9cb83904
    print("Enter a valid number")