#AREA CALCULATOR
import math
print("FIND AREA OF CALCULATOR.")
print("""Press 1 to get area of square.
press 2 to get area of circle.
press 3 to get area of rectangle.
press 4 to get area of triangle.""")
#input from user choice one number
choice = int(input("Enter any one number(1 to 4) find area: "))
if choice == 1:
    side = float(input("Enter the side of square : "))
    area = side*side
    print("Area of square = ",area)
elif choice == 2:
    r = float(input("Enter the radius of circle : "))
    area = math.pi*r**2
    print("Area of circle = ",area)
elif choice == 3:
    length = float(input("Enter the length of rectangle : "))
    width = float(input("Enter the width of rectangele : "))
    area = length*width
    print("Area of rectangle = ",area)
elif choice == 4:
    base = float(input("Enter a base of triangle : "))
    height = float(input("Enter the height of triangle : "))
    area = 0.5*base*height
    print("Area of triangle = ",area)
else:
    print("Invalid enter number.")
