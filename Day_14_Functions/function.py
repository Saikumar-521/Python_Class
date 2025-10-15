'''
built-in-functions
print()
input()
int()
str()
list()
tuple()
dict()
len()
range()
function:
this function will accepts the inputs and return the output
,it can be re-usable


function supports the :modular centric ,functional centric and data centric
'''

# function



def fun(a,b):
    return a+b

print(fun(10,20))

def volume(l,b,h):  #formal parameters :its not createing id()
    space=l*b*h
    print(id(l))
    return space
a=volume(10,5,20)  #actual parameters
print(a)


# types of parameters
# positinal parameter: all the positional arguments can be in the left side
# These are parameters that must be passed in the correct order (position) when calling the function.
# The position of each argument matters — Python matches arguments to parameters by their order.

# keyword parameter:all the keyword arguments can be in the right side
# In this case, you specify the parameter name explicitly when passing the argument.
# The order doesn’t matter, since each argument is matched by name.
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Keyword arguments
greet(age=22, name="Sai")

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
    
# Positional arguments
greet("Sai", 22)

# default arguments
'''
Default arguments are parameters that have a predefined value in a function definition.
If the caller doesn’t provide a value for that parameter, the function automatically uses the default value.
'''

def greet(name, message="Good morning"):
    print(f"Hello {name}, {message}!")
greet('sai')

'''
✅ Explanation of / (Positional-only parameters):
The slash / in a function definition means that all parameters before it can be passed only by position, not by keyword.
The parameters after / can be positional or keyword arguments.
So, in your function:
a, b, c → Positional-only parameters
d, e → Positional-or-keyword parameters
def fun2(a, b, *, c, d):
    print(a, b, c, d)
fun2(1, 2, 3, 4)

a, b → can be positional or keyword arguments
c, d → are keyword-only arguments 
'''


'''
Explanation of / (keyword-only parameters):
When you place a * in a function definition,
all parameters after the * must be passed only by keyword,
not by position.
'''





# normal positinal arg
def fun1(a,b,c,d,e):
     print(a,b,c,d,e)


fun1(1,2,3,4,5)

# 
def fun1(a,b,c,/,d,e):  #in lift side has positinal args and left side of (/) is key-word args
     print(a,b,c,d,e)

fun1(1,2,3,4,5)

# def fun1(a,b,c,/,d,e):
#     print(a,b,c,d,e)
# fun1(a=1,b=2,c=3,d=4,e=5)
# TypeError: fun1() got some positional-only arguments passed as keyword arguments: 'a, b, c'

def fun1(a,b,c,/,d,e):
    print(a,b,c,d,e,'it is positional come key word agrs')
fun1(1,2,3,d=4,e=5)

# Combined Example (/ and *):
def fun3(a, b, /, c, *, d, e):
    print(a, b, c, d, e,'its a combination of positinol and keyword args')

fun3(1,2,3,d=4,e=5)
