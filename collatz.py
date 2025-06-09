def collatz(number):
    if number % 2 == 0:
        print("Number is even")
        return number // 2
    else:
        print("Number is odd")
        return 3 * number + 1

print("Enter a number :")
number = int(input())
print(collatz(number))

def main():
    while True:
        userInput = int(input("Please enter a positive whole number : "))
        if userInput <= 0:
            print("Invalid")
            continue

        break

    print("Starting the sequence with",userInput)
    currentNumber = userInput

    while currentNumber != 1:
        currentNumber = collatz(currentNumber)

    print("Number reached to 1")

if __name__ == "__main__":
     main()