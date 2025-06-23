<<<<<<< HEAD
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
=======
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
>>>>>>> 598ff5df94d24dcf39cb65ec7081fdcd9cb83904
    print("Enter a valid number")