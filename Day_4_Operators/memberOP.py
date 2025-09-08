# member Operators: in, not in
# used to test if a sequence contains a certain element
# They are commonly used in conditional statements and loops to check for membership in strings, lists, tuples, and dictionaries.
# types of member operators:
# in : returns True if the specified element is found in the sequence
str1 = "hello world"
print("'h' in str1:", 'h' in str1)  # Output: True
print("'z' in str1:", 'z' in str1)  # Output:
print("'world' in str1:", 'world' in str1)  # Output: True False
# not in : returns True if the specified element is not found in the sequence   
print("'h' not in str1:", 'h' not in str1)  # Output: False
print("'z' not in str1:", 'z' not in str1)  # Output: True
print("'world' not in str1:", 'world' not in str1)  # Output: False
# Example with lists:
list1 = [1, 2, 3, 4, 5]   
print("3 in list1:", 3 in list1)  # Output: True
print("6 in list1:", 6 in list1)  # Output: False
print("3 not in list1:", 3 not in list1)  # Output: False
print("6 not in list1:", 6 not in list1)  # Output: True
# Example with tuples:
tuple1 = (1, 2, 3)
print("2 in tuple1:", 2 in tuple1)  # Output: True
print("4 in tuple1:", 4 in tuple1)  # Output: False
print("2 not in tuple1:", 2 not in tuple1)  # Output: False
print("4 not in tuple1:", 4 not in tuple1)  # Output: True
# Example with dictionaries:
dict1 = {'a': 1, 'b': 2, 'c': 3}
print("'a' in dict1:", 'a' in dict1)  # Output: True
print("'d' in dict1:", 'd' in dict1)  # Output: False
print("'a' not in dict1:", 'a' not in dict1)  # Output: False
print("'d' not in dict1:", 'd' not in dict1)  # Output: True
# Note: When using the 'in' operator with dictionaries, it checks for the presence of keys, not values.
# In summary, member operators are essential for checking membership in various data structures and help in making decisions in code.
# They can be used with different data types, including strings, lists, tuples, and dictionaries
# Example with sets:
set1 = {1, 2, 3, 4, 5}
print("3 in set1:", 3 in set1)  # Output: True
print("6 in set1:", 6 in set1)  # Output: False
print("3 not in set1:", 3 not in set1)  # Output: False
print("6 not in set1:", 6 not in set1)  # Output: True
# Note: Sets are unordered collections of unique elements, and the 'in' operator checks for membership in the set.
