#Home work of 13 Aug
"""Task #1
# Home Can you create a Program I will give you number(userinput and print table)
f"{}" String format concept
User input - num int -> 10, 100, -1, 2, 3.14 -> input
9x1 = 9
9x2 = 18... till 10"""


#Task 1

Tables = int(input('Enter the User Input --'))
# Tables = float(input('Enter the User Input --'))
print(Tables)
print(type(Tables))

print(f"{Tables}*1={Tables}")
print(f"{Tables}*2={Tables * 2}")
print(f"{Tables}*3={Tables * 3}")
print(f"{Tables}*4={Tables * 4}")
print(f"{Tables}*5={Tables * 5}")
print(f"{Tables}*6={Tables * 6}")
print(f"{Tables}*7={Tables * 7}")
print(f"{Tables}*8={Tables * 8}")
print(f"{Tables}*9={Tables * 9}")
print(f"{Tables}*10={Tables * 10}")



"""Task #2

Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""} """


#Task 2

num1 = int(input("Enter the num1 "))
num2 = int(input("Enter the num2 "))

print(type(num1))
print(type(num2))

"""print("Sum is", num1 + num2)
print("Maximum is", max(num1, num2))
print("Sub", num1 - num2)
print("Multi", num1 * num2)
print("Div is", num1 / num2)
print("pow", pow(num1, num2))"""

print("Sum of "f"{num1} and "f"{num2} is", num1 + num2)
print("Sub of "f"{num1} and "f"{num2} is", num1 - num2)
print("Mul of "f"{num1} and "f"{num2} is", num1 * num2)
print("div of "f"{num1} and "f"{num2} is", num1 / num2)
#doubt how to add decimal formating
print("power of "f"{num1} and "f"{num2} is", pow(num1, num2))
print("Max of "f"{num1} and "f"{num2} is", max(num1, num2))
