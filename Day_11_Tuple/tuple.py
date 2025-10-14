'''
tuple():

In Python, tuples are part of the standard language. This is a data structure very similar to the list datastructure. 
The main difference being that tuple manipulation are faster than list because tuples areimmutable.

A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.A tuple, like a list,
is a sequence of items of any type. The printed representation of a tuple is a comma-separated sequence of values, enclosed in parentheses. In other words, 
the representation is just like lists,except with parentheses () instead of square brackets [].
Tuples are a lot like lists:
Tuples are ordered
Tuples maintains a left-to-right positional ordering among the items they contain.
Accessed by index  Items in a tuple can be accessed using an index.Tuples can contain any sort of object 
– It can be numbers, strings, lists and even other tuples.except:Tuples are immutable – you can’t add, delete, or change items after the tuple is defined
'''

# Creating an empty Tuple 
Tuple1 = () 
print("Initial empty Tuple: ") 
print (Tuple1) 
print(type(Tuple1))  
#Creatting a Tuple with the use of string 
Tuple1 = ('CMR TC', 'CSE') 
print("\nTuple with the use of String: ") 
print(Tuple1)
print(type(Tuple1))   
# Creating a Tuple with the use of list 
list1 = [1, 2, 4, 5, 6] 
print("\nTuple using List: ") 
print(tuple(list1)) 
print(type(Tuple1))  
#Creating a Tuple with the use of built-in function 
Tuple1 = tuple('CMR TC') 
print("\nTuple with the use of function: ") 
print(Tuple1)
print(type(Tuple1))


# operations
# repetation
t1=(1,2,3,'tuple','sai')
print(t1)
print('tuple repetation is possible',t1*2) #(1, 2, 3, 'tuple', 'sai', 1, 2, 3, 'tuple', 'sai')

# concatination (+)
t2=(-1,0)
t2 +=t1
print(t2)
print(id(t1),'id of t1')
print(id(t2),'id of t2')
t2 +=('adding elements to tuple',)
print(t2)
print(id(t2))

'''
t2 = ()
→ Empty tuple assigned.

t2 += t1
→ Equivalent to t2 = t2 + t1.
→ A new tuple is created containing elements of t1.
→ Now t2 and t1 may or may not share the same id (depends on how t1 was defined earlier).

print(id(t1), 'id of t1')
→ Prints the memory reference (address) of t1.

print(id(t2), 'id of t2')
→ Prints the memory reference (address) of t2.
→ Even if contents are same, the id might be different because a new tuple is created.

t2 += ('adding elements to tuple',)
→ Again, new tuple is created by concatenating old t2 and ('adding elements to tuple',).
→ Notice the comma inside ('adding elements to tuple',) is very important — without it, Python treats it as just a string, not a tuple.

print(id(t2))
→ This shows a different id again, proving immutability.
'''

# tuple packing and unpacking

# tuple packing
'''
When working with multiple values or multiple variable names, 
the Python interpreter does some automaticpacking and unpacking to and from tuples,
 which allows some simplifications in the code you write
'''
T = 'red', 'green', 'blue', 'cyan'
print(T)
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# or equivalently
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
print(julia[4])
# tuple unpacking
'''
When a packed tuple is assigned to a new tuple, the individual items are unpacked (assigned to the items ofa new tuple).
Python has a very powerful tuple assignment feature that allows a tuple of variable names on the left of anassignment statement to be assigned values from a tuple on the right of the assignment. 
Another way tothink of this is that the tuple of values is unpacked into the variable names.
'''
T = ('red', 'green', 'blue', 'cyan')
(a, b, c, d) = T
print(a)
print(b)
print(c)
print(d)
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
name, surname, birth_year, movie, movie_year, profession, birth_place = julia
print(name)






# t=tuple(3)
# print(t)  #TypeError: 'int' object is not iterable
