name = input("Enter your name: ")
age = input("Enter your age: ")
number = int(input("Enter your company: "))
print(f"Your name is {name} and your age is {age} and your number is {number}",end="..")
print(f"The type of name is {type(name)} and the type of age is {type(age)} and the type of number is {type(number)}")   
#Typecasting is the process of converting one data type to another.
#In Python, we can use the built-in functions to perform typecasting.
# For example, we can convert a string to an integer using the int() function,
#  or we can convert an integer to a string using the str() function.
# Here is an example of typecasting:  
age = int(age) # converting age from string to integer
number = str(number) # converting number from integer to string
print(f"The type of age after typecasting is {type(age)}")
print(f"The type of number after typecasting is {type(number)}")

""" This is a multi-line comment. It is used to explain the code in more detail.
 It can span multiple lines and is enclosed in triple quotes."""
# This is a single-line comment. It is used to explain the code in a single line.

print("This is a single-line comment", "It is used to explain the code in a single line.", sep="/", end="\....")