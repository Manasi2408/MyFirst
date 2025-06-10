# calculator

number1 = int(input("Enter first number : "))
operand = input("Enter operand : ")
number2 = int(input("Enter second number : "))

if operand == '+':
    print("",number1,operand,number2,"=",number1+number2)
elif operand == '-':
    print("",number1,operand,number2,"=",number1-number2)
elif operand == '*':
    print("",number1,operand,number2,"=",number1*number2)
elif operand == '/':
    if number2 == 0:
        print("Error : Division by 0 is not allowed")
    else:
        print("",number1,operand,number2,"=",number1/number2)
elif operand == '%':
    if number2 == 0:
        print("Error : Modulo by 0 is not allowed")
    else:
        print("",number1,operand,number2,"=",number1%number2)
else:
    print("Invalid")

print("End of Code")