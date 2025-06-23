# vowel or consonant

while True:
    letter = input("Enter an alphabet (or 'quit' to exit): ")
    if letter.lower() == 'quit':
        break
    
    letter = letter.lower()

    if len(letter) == 1:
        if 'a' <= letter.lower() <= 'z':
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                print(letter, "is a vowel")
            else:
                print(letter, "is a consonant")   
            break
        elif '0' <= letter <= '9': 
            print(letter, "is a digit. Please enter an alphabet.")
        else:
            print(letter, "is a special character. Please enter an alphabet.")
    else:
        print("Please enter a single character.")
print("Program ended.")

# if 'a' <= letter <= 'z':

#     if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':

#         print(letter,"is a vowel")

#     else:

#         print(letter,"is a consonant")

# elif '0' <= letter <= '9':

#     print(letter,"is a digit. Please enter an alphabet")

# else:

#     print(letter,"is a special character. Please enter an alphabet")