# Generating an otp by giving phone number

import random

print("Enter your number for OTP")
number = int(input())
r = random.randint(1000,9999)
print("Your OTP is:",r)
