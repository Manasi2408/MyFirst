# enter subjects marks and display the grade, % and pass or fail

total = int(input("Total marks are out of : "))

print("How many subject ?")
subjects = int(input())

if subjects <= 0:
    print("Error")
else:
    count = subjects
    sum = 0
    print("Enter subject marks out of",total)
    while count > 0:
        marks = int(input())
        sum = sum + marks
        count -= 1
    
    upon = total * subjects
    percentage = round(((sum / upon) * 100),2)
    print()
    print("Total Marks :",sum,"/",(total*subjects))
    print("Percentage :",percentage,"%")
    if 95 <= percentage <= 100:
        print("O Grade")
    elif 90 <= percentage <= 95:
        print("A Grade")
    elif 80 <= percentage <= 90:
        print("B Grade")
    elif 70 <= percentage <= 80:
        print("B Grade")
    elif 60 <= percentage <= 70:
        print("C Grade")
    elif 40 <= percentage <= 60:
        print("D Grade")
    else:
        print("Fail")
    if 40 <= percentage <= 100:
        print("Pass")