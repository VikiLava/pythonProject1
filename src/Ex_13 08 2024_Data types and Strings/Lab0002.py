#Home work of 17 Aug

Task #3
Explain the difference between the = operator and the == operator in Python.

= operator is assignment operator
Eg : a = 5 b=5
==Operator is a comparison operator
Usually compare the value of a and b

What does the ** operator do in Python, and how is it used?
**  Refers to power of any variable or value
num = 2**3
Ans 2*2*2 = 8
print (num)


What does the ^ operator do in Python, and in what context is it commonly used?
The ^ operator compares each bit and set it to 1 if only value is 1.
else the value is set to zero if both are one or both are 0.
#1*1=0
#1*0=1
#0*1=1
#0*0=0



Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

import math
# Task 4
# Logic Build forula
"""Step 1 :
input --> r Data type--> Float , radius will be entered by the user
Py --> 3.14 or power function
Power function or **
output -- > Area of the circle with decimal numbers

Step 2 -->
Rough Logic
Area = 3.14* pow (r,2)

Step 3 Wirte the logic
"""

radius = float(input("Enter the Radius\n"))
print(radius)
print(math.pi)
Area = 3.14 * (radius**2)
print("The Area of the Circle is", Area)
print(f"The Area of Circle \n {Area:.1f}")



### Task #5

- Create a program that takes two numbers as input and prints
 whether the first number is greater than, less than, or equal to the second number.

num1 = int(input("Enter the num1"))
num2 = int(input("Enter the num2"))
if num1 > num2:
    print("Number 1 is greater than Number 2")
elif num1 == num2:
    print("Number 1 and 2 is equal ")
else:
    print("Number 2 is greater than Number 1 ")




### Task #6

- Develop a Python script that calculates the square and cube of a given number.

num1 = int(input("Enter number 1 to calculate Square\n"))
num2 = int(input("Enter number 2 to calculate Cube 1\n"))

square = num1*num1
cube = num2*num2*num2

print(f"The Square of given number 1 is {square}")
print(f"The Cube of given number  2 is {cube}")

print(f"The Square of given number 1 is {num1**2}")
print(f"The Cube of given number 1 is {num1**3}")
