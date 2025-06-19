# print first and last number

rem = 0
sum = 0

print("Enter number :")
while True:
    try:
        n = int(input())
        absN = abs(n)

        first = absN

        while first >= 10:
            first = int(first / 10)
        
        print("First :",first)

        last = absN % 10

        print("Last :",last)
        break

    except ValueError:
        print("Enter a valid number")