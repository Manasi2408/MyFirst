# password generator

import random
import string


print("Enter length of password (Alteast 4)")
length = int(input())

if length < 4:
    print("Password length must be at least 4.")
    exit()

upper = string.ascii_uppercase
lower = string.ascii_lowercase
letter = string.ascii_letters
digit = string.digits
special = string.punctuation

password = [
    random.choice(upper),
    random.choice(lower),
    random.choice(letter),
    random.choice(digit),
    random.choice(special)
]

allSet = upper + lower + letter + digit + special

for i in range(length - 4):
    password.append(random.choice(allSet))

random.shuffle(password)

final = ""
for p in password:
    final += p

print("Generated password :",final)