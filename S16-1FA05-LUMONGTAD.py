# We first need to import math, so we can do calculations.
import math

# We will find the value or input the value of the variables here.
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# This is the formula for distance.
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Finally we will print the final answer in 2 decimal points (.2f) 
print(f"\nThe distance between the two points is: {distance:.2f}")

# Using a library in important so that we can use the functions to do complex calculations. Examples of these functions include sqrt and pow.
