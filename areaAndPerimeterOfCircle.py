# calculate the area and perimeter of a circle

import math

radius = float(input("Enter radius of the circle : "))

perimeter = 2 * round(math.pi,2) * radius 
area = round(math.pi,2) * radius * radius

print("Perimeter :",perimeter)
print("Area :",area)