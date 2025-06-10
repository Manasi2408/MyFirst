import sys

print("M to CM press 1 or CM to M press 2")

convert = int(input("Pressing : "))

print()

if convert == 1:
        print("M to CM conversion :")
        meter = float(input("Enter M : "))

        centimeter = meter * 100 

        print(meter,"M is",centimeter,"CM")

elif convert == 2:
        print("CM to M conversion :")
        centimeter = float(input("Enter CM : "))

        meter = centimeter / 100

        print(centimeter,"CM is",meter,"M")
else:
        print("Error")