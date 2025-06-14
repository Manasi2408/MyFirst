# calculate simple interest

import sys

print("Calculate simple interest")

print("Convert months to years if you want to:(yes/no)")
ans = input()
ans = ans.lower()
if ans == 'yes':
    months = int(input("Enter months : "))
    year = round((months / 12),1)
    print("",months,"month(s) to years is",year)
else:
    ans == 'no'
    sys.exit

principal = float(input("Principal amount : "))
rate = float(input("Rate of interest : "))
number = float(input("Number of years : "))
simple = (principal * rate * number) / 100

print("Simple Interest :",simple)