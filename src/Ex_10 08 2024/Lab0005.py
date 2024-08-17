#Since it is String we cant compare Int with Str

#print(max(30, 150 , -55.25 , 55, "Pramod"))-- TypeError: '>' not supported between instances of 'str' and 'int'

#We cant use below reserved keywords as variables

import keyword
from collections.abc import AsyncGenerator
from tkinter.tix import INTEGER

print(keyword.kwlist)

#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#Variables are Containers - Used to Store Values

age = 65
print(age)
age = 100
#Type --- INTEGER
#Varaible Name ---> Age
#Vaule --> 65
print(age)
age = "Vignesh"
print(age)

#Variable name = Value value

