#conditional statements
# Conditional statements are used to perform different actions based on different conditions.
# They allow you to control the flow of your program by executing certain blocks of code only when specific conditions are met.
# The most common conditional statements in Python are if, elif, and if else.and match
# Here are some examples of conditional statements in Python:
a = 10
b = 20
if a < b:
    print("a is less than b")
if a > b:
    print("a is greater than b")
if a == b:
    print("a is equal to b")
if a != b:
    print("a is not equal to b")
if a <= b:
    print("a is less than or equal to b")
if a >= b:
    print("a is greater than or equal to b")
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 3}
print("dict1 == dict2:", dict1 == dict2)  # Output: False
print("dict1 != dict2:", dict1 != dict2)  # Output: True
print("dict1 < dict2:", dict1 < dict2)    # Output: True
print("dict1 > dict2:", dict1 > dict2)    # Output: False
print("dict1 <= dict2:", dict1 <= dict2)  # Output: True
print("dict1 >= dict2:", dict1 >= dict2)  # Output: False
# Note: When comparing dictionaries, the comparison is done based on the key-value pairs.

# Example with sets:
set1 = {1, 2, 3}
set2 = {1, 2, 4}
print("set1 == set2:", set1 == set2)  # Output: False
print("set1 != set2:", set1 != set2)  # Output: True
# Note: Sets are unordered collections, so comparison operators like <, >, <=, >= are not applicable to sets.
# In summary, comparison operators are essential for making decisions in code and controlling the flow of execution

# based on the relationships between values.
# They can be used with various data types, including integers, floats, strings, lists, tuples, dictionaries, and sets.
# They are commonly used in conditional statements and loops to control the flow of a program based on certain conditions.
# Here are the common comparison operators in Python:
# types of comparison operators:
# == : checks if two values are equal
a = 5
b = 10
print("a == b:", a == b)  # Output: False
# != : checks if two values are not equal
print("a != b:", a != b)  # Output: True    

#if-else statement
# The if-else statement is a fundamental control structure in programming that allows you to execute different
# blocks of code based on whether a specified condition is true or false.
# The basic syntax of an if-else statement in Python is as follows:
# if condition:
#     # code to be executed if the condition is true
# else:
#     # code to be executed if the condition is false
# Here are some examples of if-else statements in Python:
x = 15
if x % 2 == 0:
    print("x is an even number")
else:
    print("x is an odd number")
age = 18
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
temperature = 25
if temperature > 30:
    print("It's a hot day")
else:
    print("It's a cool day")

# Example with nested elif statements:
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C or below")
# Example with multiple conditions using logical operators:
num = 15
if num > 0 and num < 20:
    print("num is a positive number less than 20")
else:
    print("num is either negative or 20 or greater")
# Example with strings:
name = "Alice"
if name == "Alice":
    print("Hello, Alice!")
else:
    print("Hello, stranger!")
# Example with lists:
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")  
else:
    print("Banana is not in the list")
# Example with tuples:
point = (3, 4)
if point == (0, 0):
    print("The point is at the origin")
else:
    print("The point is not at the origin")

number= int(input("Enter a number: "))
if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")
