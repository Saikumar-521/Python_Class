
'''
hf
sai kumer
ggydyu
'''
#what is variable?
# A variable is a container that holds data or a value in a program. It is used to store and manipulate information during the execution of a program.
#variables are used to store the address of the data in the memory.
#variables are used to store the value of the data in the memory.

#rules for declaring a variable
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords


#data types in python
#primitives:
#primitive data types are store the single value and it is immutable
#1.int
#2.float
#3.complex
#4.bool
#non-primitives:
#non-primitive data types are store the multiple values and it is mutable
#1.str
#2.list
#3.tuple
#4.set
#5.dict

#sequence data types:
#1.list
#2.tuple
#3.range
#non-sequence data types:
#1.str
#2.set
#3.dict

#mutable data types:
#defined as the data types that can be changed after they are created.that is we can add,remove,update the values.
# without creating a new object.and it is also called as non-primitive data types. affected by reference.
#1.list
#2.set
#3.dict
#immutable data types:
#defined as the data types that cannot be changed after they are created.that is we cannot add,remove,update the values.
# without creating a new object. and it is also called as primitive data types. affected by value.
#1.int
#2.float
#3.complex
#4.bool
#5.str
#6.tuple


variable_name = "sai kumar" #variable declaration and initialization
# single line comment
'''This is a multi-line comment '''  # multi line comment if we assign this multi line comment to a variable it will be treated as a string
print(variable_name)

#types of declarations
#1. single variable declaration
x = 10
#2. multiple variable declaration
a, b, c = 1, 2, 3
#3. single value to multiple variable declaration
m = n = o = 5
print(x)
print(a, b, c)
print(m, n, o)


#interview question on variable and data types in python
"""1. What is a variable in Python?
A variable in Python is a named location used to store data in the memory. It acts as a container that holds a value, which can be of various data types such as integers, strings, lists, etc. 
Variables are created when they are first assigned a value, and they can be reassigned to different values throughout the program.

2. How do you declare and initialize a variable in Python?
In Python, you can declare and initialize a variable by simply assigning a value to it using the assignment operator (=). For example:
x = 10  # Declares and initializes an integer variable

3. What are the rules for naming variables in Python?
- A variable name must start with a letter (a-z, A-Z) or an underscore (_).
- A variable name cannot start with a number (0-9).
- A variable name can only contain alphanumeric characters (letters and numbers) and underscores.
- Variable names are case-sensitive (e.g., myVar and myvar are different variables).
- You cannot use Python reserved keywords as variable names (e.g., if, else, while, etc.).

4. What are the different data types in Python?
Python has several built-in data types, including:
primitives: 
numberic types: int, float, complex
boolean type: bool
non-primitives: str, list, tuple, set, dict

5. How do you check the data type of a variable in Python?
You can check the data type of a variable in Python using the built-in type() function. For example:
x = 10
print(type(x))  # Output: <class 'int'>

6. What is the difference between a variable and a constant?
A variable is a named location in memory that can hold different values during the execution of a program
and can be changed or reassigned. A constant, on the other hand, is a value that is meant to remain unchanged throughout the program. In Python, there is no built-in constant type, but by convention, constants are usually defined using uppercase letters (e.g., PI = 3.14) to indicate that they should not be modified.

7. Can a variable name contain special characters or spaces?
No, a variable name cannot contain special characters (e.g., @, #, $, %, etc.) or spaces. It can only contain alphanumeric characters (letters and numbers) and underscores (_).

8. How do you assign multiple values to multiple variables in a single line in Python?
You can assign multiple values to multiple variables in a single line using tuple unpacking. For example:
x, y, z = 1, 2, 3  # Assigns 1 to x, 2 to y, and 3 to z

9. What is the difference between mutable and immutable data types in Python?
Mutable data types are those that can be changed or modified after they are created, 
while immutable data types cannot be changed once they are created. Examples of mutable data types include lists, dictionaries, and sets, while examples of immutable data types include strings, tuples, and frozensets.

10. How do you delete a variable in Python?
You can delete a variable in Python using the del statement. For example:
x = 10
del x  # Deletes the variable x
print(x)  # This will raise a NameError since x has been deleted

11.explain about type casting in python?
Type casting in Python refers to the process of converting a variable from one data type to another. 
This can be done using built-in functions such as int(), float(), str(), list(), tuple(), etc.

12.Explain about dynamic typing in python?
Dynamic typing in Python means that the type of a variable is determined at runtime, and you do not need to explicitly declare the type of a variable when you create it.
This allows for greater flexibility in programming, as you can easily change the type of a variable by assigning a new value to it.

13. What are some common built-in functions in Python for working with variables and data types?
Some common built-in functions in Python for working with variables and data types include:
- type(): Returns the data type of a variable
- isinstance(): Checks if a variable is of a specific data type
- len(): Returns the length of a sequence (e.g., string, list, tuple)
- str(), int(), float(): Type casting functions to convert between data types
- input(): Reads input from the user and returns it as a string
- print(): Outputs data to the console

14.Explain about primitive and non-primitive data types in python?
Primitive data types in Python are the basic data types that are built into the language and represent simple values. They include:
- int: Represents integer values (e.g., 1, 2, 3)
- float: Represents floating-point values (e.g., 1.0, 2.5, 3.14)
- complex: Represents complex numbers (e.g., 1 + 2j)    
- bool: Represents boolean values (True or False)
Non-primitive data types, on the other hand, are more complex data structures that can hold multiple values or objects. They include:
- str: Represents strings, which are sequences of characters (e.g., "Hello, World)
- list: Represents ordered collections of items that can be of different data types (e.g.,) [1, "Hello", 3.14])
- tuple: Represents ordered, immutable collections of items (e.g., (1, "Hello", 3.14))
- set: Represents unordered collections of unique items (e.g., {1, 2, 3})
- dict: Represents key-value pairs, where each key is unique (e.g., {"name": "Alice", "age": 30})
#15. What is the difference between sequence and non-sequence data types in Python?
Sequence data types in Python are data types that store multiple values in a specific order, allowing for indexing and slicing. Examples of sequence data types include:
- list: An ordered, mutable collection of items (e.g., [1, 2, 3])
- tuple: An ordered, immutable collection of items (e.g., (1, 2, 3))
- range: Represents a sequence of numbers, commonly used in loops (e.g., range(5) produces 0, 1, 2, 3, 4)
Non-sequence data types, on the other hand, do not maintain any specific order of elements and do not support indexing or slicing. Examples of non-sequence data types include:
- str: Although strings are sequences of characters, they are often treated as non-sequence data types in certain contexts because they are immutable.
- set: An unordered collection of unique items (e.g., {1, 2, 3})
- dict: A collection of key-value pairs, where each key is unique (e.g., {"name": "Alice", "age": 30})
#16. How do you check the memory address of a variable in Python?
You can check the memory address of a variable in Python using the built-in id() function. For example:
x = 10
print(id(x))  # Output: Memory address of the variable x

"""
#What is the difference between a variable and a constant?
#What are the different data types in Python?
#The different data types in Python are:
#1. Numeric types: int, float, complex
#2. Sequence types: list, tuple, range
#3. Text type: str
#4. Set types: set, frozenset
#5. Mapping type: dict
#6. Boolean type: bool
#7. Binary types: bytes, bytearray, memoryview
#8. None type: NoneType

name = "sai kumar" #string
age = 21 #int
height = 5.9 #float
is_student = True #bool
complex_num = 2 + 3j #complex
fruits = ["apple", "banana", "cherry"] #list
person = {"name": "sai kumar", "age": 21} #dict

#The type() function in Python is used to get the data type of an object.
print(type(name)) # <class 'str'>
print(type(age))    # <class 'int'>
print(type(height)) # <class 'float'>
print(type(is_student)) # <class 'bool'>
print(type(complex_num)) # <class 'complex'>
print(type(fruits)) # <class 'list'>
print(type(person)) # <class 'dict'>

#The id() function in Python is used to get the unique identifier (memory address) of an object.
print(id(name)) #prints the memory address of the variable
print(id(age)) #prints the memory address of the variable
print(id(height)) #prints the memory address of the variable
print(id(is_student)) #prints the memory address of the variable
print(id(complex_num)) #prints the memory address of the variable
print(id(fruits)) #prints the memory address of the variable
print(id(person)) #prints the memory address of the variable

#The del statement in Python is used to delete a variable or an object.
del person
#print(person) #This will raise a NameError since person has been deleted

print(name.upper()) #prints the string in uppercase
Name =name.upper() #converts the string to uppercase
print(Name) #prints the string in uppercase


x = "Python "
y = "is "
print(id(y)) #prints the memory address of the variable
z = "awesome"
print(x + y + z) #prints the concatenated string


x = 5
y = "John"
print(id(y)) #prints the memory address of the variable
print(x, y,x,y,z) #prints the integer and string with a space in between