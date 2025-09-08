# comparision operators are used to compare two values or expressions and return a boolean result (True or False).
# They are commonly used in conditional statements and loops to control the flow of a program based on certain conditions.
# Here are the common comparison operators in Python:
# types of comparison operators:
# == : checks if two values are equal
a = 5
b = 10
print("a == b:", a == b)  # Output: False

# != : checks if two values are not equal
print("a != b:", a != b)  # Output: True

# > : checks if the left value is greater than the right value
print("a > b:", a > b)    # Output: False

# < : checks if the left value is less than the right value
print("a < b:", a < b)    # Output: True

# >= : checks if the left value is greater than or equal to the right value
print("a >= b:", a >= b)  # Output: False

# <= : checks if the left value is less than or equal to the right value
print("a <= b:", a <= b)  # Output: True

# Example with strings:
str1 = "hello"
str2 = "world"
print("str1 == str2:", str1 == str2)  # Output: False
print("str1 != str2:", str1 != str2)  # Output: True
print("str1 < str2:", str1 < str2)    # Output: True
print("str1 > str2:", str1 > str2)    # Output: False
print("str1 <= str2:", str1 <= str2)  # Output: True
print("str1 >= str2:", str1 >= str2)  # Output: False


# Example with lists:
list1 = [1, 2, 3]
list2 = [1, 2, 4]
print("list1 == list2:", list1 == list2)  # Output: False

print("list1 != list2:", list1 != list2)  # Output: True
print("list1 < list2:", list1 < list2)    # Output: True
print("list1 > list2:", list1 > list2)    # Output: False
print("list1 <= list2:", list1 <= list2)  # Output: True
print("list1 >= list2:", list1 >= list2)  # Output: False
# Note: When comparing complex data types like lists and strings, the comparison is done lexicographically (dictionary order).
# In summary, comparison operators are essential for making decisions in code and controlling the flow of execution
# based on the relationships between values.
# They can be used with various data types, including integers, floats, strings, and lists
# Example with tuples:
tuple1 = (1, 2)
tuple2 = (1, 3)
print("tuple1 == tuple2:", tuple1 == tuple2)  # Output: False
print("tuple1 != tuple2:", tuple1 != tuple2)  # Output: True
print("tuple1 < tuple2:", tuple1 < tuple2)    # Output: True
print("tuple1 > tuple2:", tuple1 > tuple2)    # Output: False
print("tuple1 <= tuple2:", tuple1 <= tuple2)  # Output: True
print("tuple1 >= tuple2:", tuple1 >= tuple2)  # Output: False

# Example with dictionaries:
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 3}
print("dict1 == dict2:", dict1 == dict2)  # Output: False
print("dict1 != dict2:", dict1 != dict2)  # Output: True
print("dict1 < dict2:", dict1 < dict2)    # Output: Error (dictionaries do not support < or > comparisons)
print("dict1 > dict2:", dict1 > dict2)    # Output: Error
print("dict1 <= dict2:", dict1 <= dict2)  # Output: Error
print("dict1 >= dict2:", dict1 >= dict2)  # Output: Error
# Note: Dictionaries do not support <, >, <=, >= comparisons directly, so attempting to use these operators will result in a TypeError.
# Instead, you can compare dictionaries by comparing their items or keys if needed.
# For example, you can compare the keys of two dictionaries:
print("dict1.keys() == dict2.keys():", dict1.keys() == dict2.keys())  # Output: True
print("dict1.keys() != dict2.keys():", dict1.keys() != dict2.keys())  # Output: False
# In summary, comparison operators are essential for making decisions in code and controlling the flow of execution
# based on the relationships between values.
# They can be used with various data types, including integers, floats, strings, lists, tuples, and dictionaries (with some limitations for dictionaries).
# Example with sets:
set1 = {1, 2, 3}
set2 = {1, 2, 4}
print("set1 == set2:", set1 == set2)  # Output: False
print("set1 != set2:", set1 != set2)  # Output: True
# Note: Sets do not support <, >, <=, >= comparisons directly, so attempting
# to use these operators will result in a TypeError.
# Instead, you can compare sets using methods like issubset() and issuperset()
print("set1.issubset(set2):", set1.issubset(set2))  # Output: False
print("set1.issuperset(set2):", set1.issuperset(set2))  # Output: False
# In summary, comparison operators are essential for making decisions in code and controlling the flow of execution
# based on the relationships between values.
# They can be used with various data types, including integers, floats, strings, lists, tuples, and dictionaries (with some limitations for dictionaries).
# Example with booleans:
bool1 = True
bool2 = False
print("bool1 == bool2:", bool1 == bool2)  # Output: False
print("bool1 != bool2:", bool1 != bool2)  # Output: True
print("bool1 > bool2:", bool1 > bool2)    # Output: True
print("bool1 < bool2:", bool1 < bool2)    # Output: False
print("bool1 >= bool2:", bool1 >= bool2)  # Output: True
print("bool1 <= bool2:", bool1 <= bool2)  # Output: False
# Note: In Python, True is considered greater than False when using comparison operators.
# In summary, comparison operators are essential for making decisions in code and controlling the flow of execution
# based on the relationships between values.
# They can be used with various data types, including integers, floats, strings, lists, tuples, dictionaries (with some limitations for dictionaries), sets (with some limitations for sets), and booleans.
# Example with mixed data types:
print("a == 5.0:", a == 5.0)  # Output: True (int and float comparison)
print("a != 5.0:", a != 5.0)  # Output: False
print("a < 10.0:", a < 10.0)    # Output: True
print("a > 10.0:", a > 10.0)    # Output: False
print("a <= 5.0:", a <= 5.0)  # Output: True
print("a >= 5.0:", a >= 5.0)  # Output: True
# Note: Python allows comparison between different numeric types (int, float) seamlessly.   However, comparing non-numeric types (like int and str) will result in a TypeError.
# In summary, comparison operators are essential for making decisions in code and controlling the flow of execution     
# based on the relationships between values.
# They can be used with various data types, including integers, floats, strings, lists, tuples, dictionaries (with some limitations for dictionaries), sets (with some limitations for sets), and booleans.
# Example with None:    
print("a == None:", a == None)  # Output: False
print("a != None:", a != None)  # Output: True  
print("None == None:", None == None)  # Output: True
print("None != None:", None != None)  # Output: False
print("None < 1:", None < 1)    # Output: Error (TypeError)
print("None > 1:", None > 1)    # Output: Error (TypeError)
print("None <= 1:", None <= 1)  # Output: Error (TypeError)
print("None >= 1:", None >= 1)  # Output: Error (TypeError)
# Note: None can only be compared for equality or inequality. Attempting to use <, >, <=, >= with None will result in a TypeError.
# In summary, comparison operators are essential for making decisions in code and controlling the flow of execution
# based on the relationships between values.
# They can be used with various data types, including integers, floats, strings, lists, tuples, dictionaries (with some limitations for dictionaries), sets (with some limitations for sets), booleans, and None (with limitations).
# Example with custom objects:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, Person):
            return self.age <= other.age
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, Person):
            return self.age >= other.age
        return NotImplemented
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
print("person1 == person2:", person1 == person2)  # Output: False
print("person1 != person2:", person1 != person2)  # Output: True
print("person1 < person2:", person1 < person2)    # Output: False
print("person1 > person2:", person1 > person2)    # Output: True
print("person1 <= person2:", person1 <= person2)  # Output: False   
print("person1 >= person2:", person1 >= person2)  # Output: True
# Note: To use comparison operators with custom objects, you need to define the appropriate special methods (__eq__, __ne__, __lt__, __le__, __gt__, __ge__) in the class.


