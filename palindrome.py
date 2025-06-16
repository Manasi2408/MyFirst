# palindrome number

sum = 0
temp = 0
rem = 0

print("Palindrome number check ")
print("Enter number :")
try:
    number = int(input())

    temp = number

    while temp != 0:
        rem = temp % 10
        sum = sum * 10 + rem
        temp = int(temp / 10)

    if sum == number:
        print(number,"is a palindrome number")
    else:
        print(number,"is not a palindrome number")
except ValueError:
    print("Enter a valid number")