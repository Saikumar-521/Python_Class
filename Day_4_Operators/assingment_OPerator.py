# Assingment Operators
# default assignment operator is '='
# it assigns the value on the right to the variable on the left
# example:
x = 5
y = 10
print("Initial values:")
print("x =", x)
print("y =", y)
# Output: x = 5, y = 10
# You can also use augmented assignment operators to perform operations and assign the result to the same variable
# Types of augmented assignment operators:
# += : adds the right operand to the left operand and assigns the result to the left operand
x += 3  # equivalent to x = x + 3
print("\nAfter x += 3:")
print("x =", x)  # Output: x = 8
# -= : subtracts the right operand from the left operand and assigns the result to the left operand
y -= 2  # equivalent to y = y - 2       
print("\nAfter y -= 2:")
print("y =", y)  # Output: y = 8
# *= : multiplies the left operand by the right operand and assigns the result to the left operand
x *= 2  # equivalent to x = x * 2
print("\nAfter x *= 2:")
print("x =", x)  # Output: x = 16
# /= : divides the left operand by the right operand and assigns the result to the left operand
y /= 4  # equivalent to y = y / 4
print("\nAfter y /= 4:")
print("y =", y)  # Output: y = 2.0
# %= : takes the modulus of the left operand by the right operand and assigns the result to the left operand
x %= 5  # equivalent to x = x % 5
print("\nAfter x %= 5:")
print("x =", x)  # Output: x = 1
# **= : raises the left operand to the power of the right operand and assigns the result to the left operand
y **= 3  # equivalent to y = y ** 3
print("\nAfter y **= 3:")
print("y =", y)  # Output: y = 8.0
# //= : performs floor division on the left operand by the right operand and assigns the result to the left operand
x //= 2  # equivalent to x = x // 2
print("\nAfter x //= 2:")
print("x =", x)  # Output: x = 0
# These operators help to simplify code and make it more readable
# You can use these operators with different data types like integers, floats, and strings (for concatenation)
# Example with strings:
str1 = "Hello"
str2 = " World"
str1 += str2  # equivalent to str1 = str1 + str2
print("\nAfter str1 += str2:")
print("str1 =", str1)  # Output: str1 = Hello World
# Example with lists:
list1 = [1, 2, 3]   
list2 = [4, 5, 6]
list1 += list2  # equivalent to list1 = list1 + list2
print("\nAfter list1 += list2:")
print("list1 =", list1)  # Output: list1 = [1, 2, 3, 4, 5, 6]
# Note: Be cautious when using augmented assignment operators with mutable data types like lists and dictionaries,
# as they modify the original object rather than creating a new one.
# Example with dictionaries:
dict1 = {'a': 1, 'b': 2}
print(id(dict1))
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)  # equivalent to dict1 = {**dict1, **dict2}
print("\nAfter dict1.update(dict2):")
print("dict1 =", dict1)  # Output: dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(id(dict1))
# Note: Dictionaries do not support the += operator directly, so we use the update() method
# In summary, assignment operators are essential for variable manipulation and help in writing concise and efficient code
# Example with tuples:
tuple1 = (1, 2)
print(id(tuple1))
tuple2 = (3, 4)
tuple1 += tuple2  # equivalent to tuple1 = tuple1 + tuple2
print("\nAfter tuple1 += tuple2:")
print("tuple1 =", tuple1)  # Output: tuple1 = (1, 2, 3, 4)
print(id(tuple1))
# Note: Tuples are immutable, so this operation creates a new tuple rather than modifying the
# original one.

