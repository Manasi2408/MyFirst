# # name middle name and last name 

print("Enter your full name: ")
fullName = input()

nameParts = fullName.split()

firstName = ""
middleName = ""
lastName = ""

if len(nameParts) == 1:
    firstName = nameParts[0]

elif len(nameParts) == 2:
    firstName = nameParts[0]
    lastName = nameParts[1]

elif len(nameParts) >= 3:
    firstName = nameParts[0]
    middleName = nameParts[1]
    lastName = nameParts[-1]

else:
    print("No name entered .")

fullName = fullName.upper()
firstName = firstName.upper()
middleName = middleName.upper()
lastName = lastName.upper()

if fullName and firstName:
    print("Full Name :",fullName)
    print("First Name :",firstName)

if middleName:
    print("Middle Name :",middleName)

if lastName:
    print("Last Name :",lastName)

# # # End of Code # # #