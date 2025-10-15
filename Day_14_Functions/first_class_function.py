'''
A first-class function (or first-class citizen) is a function that is treated like any other object 
in a programming language.
This means functions can be:
Assigned to variables
Passed as arguments to other functions
Returned from other functions
Stored in data structures (like lists or dictionaries)
'''
# assign a function to a variable
def fun(name):
    return f'hello,{name}?'
variable=fun  #here function assigned to a variable
print(variable('sai'))

# passing a function as an argumet
def passing_function(text):
    return text.upper()

def main_function(t):
    print(passing_function('this a function passing as argument from main functio'))

main_function(passing_function)

# returning a function from another function,
def outter():
    def inner():
        return 'inner function called'
    return inner # returning function, not calling it

r=outter()
print(r())  #here inner function will celled or invoked
print(type(r))
# print(r) #


# Stored in data structures (like lists or dictionaries)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
l1=[add,sub]
for function in l1:
    print(function(10,20))

print(l1[0](1,2))  #here first accessing the list then calling the index--0 position function and passing two parameters
print(l1[1](20,10))


# with dict
def greet():
    return 'hello'
def bye():
    return 'goodbye!'
action={
    'morning':greet,
    'evening':bye
}
print(action['morning']())
print(action['evening']())
# Functions are stored as values in a dictionary.
# You can easily pick and call them using keys — just like accessing data.


'''
advantages:
Why Use Functions that Return Functions?

There are many powerful uses:
Encapsulation – hide inner logic
Closures – inner function remembers values from the outer function
Decorators – add extra features to functions dynamically
Dynamic function creation – return a function based on certain conditions
'''