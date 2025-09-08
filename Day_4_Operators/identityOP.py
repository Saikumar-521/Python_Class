# identity operators are used to compare the memory locations of two objects.
# They are commonly used to check if two variables point to the same object in memory.
# Here are the common identity operators in Python:
# types of identity operators:
# is : returns True if both variables point to the same object
a = [1, 2, 3]
b = a
print("a is b:", a is b)  # Output: True    
c = [1, 2, 3]
print("a is c:", a is c)  # Output: False
# is not : returns True if both variables do not point to the same object
print("a is not b:", a is not b)  # Output: False
print("a is not c:", a is not c)  # Output: True
# Example with strings:
str1 = "hello"
str2 = str1
print("str1 is str2:", str1 is str2)  # Output: True
str3 = "hello"
print("str1 is str3:", str1 is str3)  # Output: True
print("str1 is not str3:", str1 is not str3)  # Output: False
# Example with integers:
num1 = 100
num2 = num1
print("num1 is num2:", num1 is num2)  # Output: True
num3 = 100
print("num1 is num3:", num1 is num3)  # Output: True
print("num1 is not num3:", num1 is not num3)  # Output: False
# Note: In Python, small integers and short strings are cached for performance reasons, so they may point to the same object in memory.
# However, this behavior should not be relied upon for identity checks.
# In summary, identity operators are essential for checking object identity and memory management in Python.