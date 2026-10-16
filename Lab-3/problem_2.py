from math import sqrt
point1 = input("Enter first point: ")
x1, y1 = point1.split(",")
x1 = float(x1)
y1 = float(y1)

point2 = input("Enter 2nd point: ")
x2, y2 = point2.split(",")
x2 = float(x2)
y2 = float(y2)

distance = sqrt((x2-x1)**2+(y2-y1)**2)

print("Distance:", distance)