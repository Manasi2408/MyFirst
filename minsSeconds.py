# convert minutes to hours vise versa

print("For hours => minutes press 'h' ")
print("For minutes => hours press 'm'")

convert = input()

if convert == 'h':
    hours = float(input("Enter hours : "))
    hourToMinute = hours * 60
    print("",hours,"hours is",hourToMinute,"minutes")

elif convert == 'm':
    mins = float(input("Enter minutes : "))
    minuteToHour = mins / 60
    print("",mins,"minutes is",minuteToHour,"hours")
    
else:
    print("Error")