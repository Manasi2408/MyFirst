# digital, letter or special character

press = input("Press any key: ")

if 'a' <= press <= 'z':
    print(press,"is a letter")

elif '0' <= press <= '9':
    print(press,"is a digit")

else:
    print(press,"is a special character")