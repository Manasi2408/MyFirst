<<<<<<< HEAD
# calculate average of number

print("Average of numbers :")

totNum = int(input("How many numbers : "))

if totNum <= 0:
    print("Please enter positive number !")
else:
    count = totNum
    sum = 0
    print("Enter numbers :")
    while count > 0:
        number = int(input())
        sum += number
        count -= 1
    average = (sum/totNum)

=======
# calculate average of number

print("Average of numbers :")

totNum = int(input("How many numbers : "))

if totNum <= 0:
    print("Please enter positive number !")
else:
    count = totNum
    sum = 0
    print("Enter numbers :")
    while count > 0:
        number = int(input())
        sum += number
        count -= 1
    average = (sum/totNum)

>>>>>>> 598ff5df94d24dcf39cb65ec7081fdcd9cb83904
    print("Average of",totNum,"numbers is",average)