# This is a simple calculator used to solve quadratic equations
# Author: Logan Gremler 11/5/15

# Import the Square Root function from the math module:
from math import sqrt

# Provide the user with the standard format for the equation as reference:
print "Quadratic equations: ax^2+bx+c=0"

# Figure out what the missing values are by having the user input them:
a = input("What is the value of variable a? ")
b = input("What is the value of variable b? ")
c = input("What is the value of variable c? ")

# Store the discriminant:
discriminant = b**2-4*a*c

# Solve the equation and display the appropriate answer(s) for the user:
if discriminant == 0:
    equation1 = (-b + sqrt(b**2-4*a*c)) / (2*a)
    print "Equation: " +str(a)+ "x^2+" +str(b)+ "x+" +str(c)+ "=0 has one solution."
    print "Solution 1:", equation1
elif discriminant > 0:
    equation1 = (-b + sqrt(b**2-4*a*c)) / (2*a)
    equation2 = (-b - sqrt(b**2-4*a*c)) / (2*a)
    print "Equation: " +str(a)+ "x^2+" +str(b)+ "x+" +str(c)+ "=0 has two solutions."
    print "Solution 1:", equation1
    print "Solution 2:", equation2
else:
    print "Equation: " +str(a)+ "x^2+" +str(b)+ "x+" +str(c)+ "=0 has no solutions."

