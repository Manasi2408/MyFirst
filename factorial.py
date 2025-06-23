# factorial of any number

print("Enter a number :")
while True:
    try:
        n = int(input())
        if n < 0:
            print("Factorial cannot be defined for negative numbers")
            continue

        fact = 1
        for i in range(1,n+1):
            fact *= i
        print("Factorial of",n,"is",fact)
        break
    except ValueError:
        print("Enter a positive digit")