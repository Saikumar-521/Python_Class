# logical operators are used to combine conditional statements
# They are commonly used in conditional statements and loops to control the flow of a program based on certain conditions.
# Here are the common logical operators in Python:  
# types of logical operators:
# and : returns True if both statements are true
a = 5
b = 10
c = 15
print("a < b and b < c:", a < b and b < c)  # Output: True
print("a < b and b > c:", a < b and b > c)  # Output: False
# or : returns True if one of the statements is true
print("a < b or b > c:", a < b or b > c)
print("a > b or b > c:", a > b or b > c)  # Output: False
# not : reverses the result, returns False if the result is true
print("not(a < b):", not(a < b))  # Output: False
print("not(a > b):", not(a > b))  # Output: True
# Example with strings:
str1 = "hello"
str2 = "world"
print("str1 == 'hello' and str2 == 'world':", str1 == 'hello' and str2 == 'world')  # Output: True
print("str1 == 'hello' or str2 == 'python':", str1 == 'hello' or str2 == 'python')  # Output: True
print("not(str1 == 'hello'):", not(str1 == 'hello'))  # Output: False
# Example with lists:
list1 = [1, 2, 3]   
list2 = [4, 5, 6]
print("len(list1) == 3 and len(list2) == 3:", len(list1) == 3 and len(list2) == 3)  # Output: True
print("len(list1) == 3 or len(list2) == 2:", len(list1) == 3 or len(list2) == 2)  # Output: True
print("not(len(list1) == 3):", not(len(list1) == 3))  # Output: False
# Note: Logical operators can be combined to form complex expressions
# Example of complex expression:
x = 5
y = 10
z = 15
result = (x < y and y < z) or (x > y and y > z)
print("Complex expression result:", result)  # Output: True
