# swaping of two number susing 2 or 3 variables

print("Enter two numbers: ")

n1 = int(input())
n2 = int(input())

n3 = 0

n3 = n1
n1 = n2
n2 = n3

print(n1,n2)

print("---------------------------------------------------------")

n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2

print(n1,n2)