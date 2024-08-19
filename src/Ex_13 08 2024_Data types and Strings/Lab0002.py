#Home work of 17 Aug

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
