'''functiona as Objects
    2.nested functions
    3.functions as arguments or passing a functions as a parameter(higer order functions)
    4.lamda functions (anonymous functions):defined using lambda keyword
    5.closures (higher order functions)
    6.decorators

'''
# 1.Functions as Objects
import re
from numpy import outer


def square(x):
    return x * x
print(square(5))
print(type(square))
print(id(square))
print(id(square(5)))
print(square.__name__)
print(dir(square))
print(help(square))


# 2.nested functions
def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    inner_function()    
outer_function()
# inner_function() # NameError: name 'inner_function' is not defined
# we can return inner function
def outer_function():       
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")
    return inner_function
# inner_func = outer_function()
# inner_func()
outer_function() #excutes outer function and returns inner function
# outer_function()() # we can call it like this also

# 3.functions as arguments or passing a functions as a parameter(higer order functions)
def square(x):
    return x * x
def cube(x):
    return x * x * x
def outer_function(func, value): # func is parameter
    return func(value) # func is used as a function
print(outer_function(square, 5)) # square is argument
print(outer_function(cube, 5))


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def cal(f,x,y):
    return f(x,y)
print(cal(add,5549,454))


# closures (higher order functions): defined as a function that returns another function and the returned function remembers the values of the variables of the outer function even after the outer function has finished executing.
# A closure is a function object that has access to variables in its enclosing lexical scope, even when the function is called outside that scope.
# closures are used to create decorators, which are functions that modify the behavior of other functions.

def outer_function(msg):
    print("This is the outer function and the msg is",msg)
    def inner_function():
        print(msg)
    print('*'*10)
    return inner_function
    
hi_func = outer_function("Hi")
hello_func = outer_function("Hello")
hi_func()
hello_func()

# 4.lamda functions (anonymous functions):defined using lambda keyword
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# syntax: lambda arguments: expression
# lambda function can have any number of arguments but only one expression
# lambda functions are used for short period of time, where we need a small function for a short period of time.
# lambda functions are used in higher order functions like map(), filter(), reduce() etc.
# map() function takes two arguments, a function and a iterable (like a list, tuple etc.) and returns an iterator that applies the function to every item of the iterable.
# filter() function takes two arguments, a function and a iterable and returns an iterator that contains only the items for which the function returns True.
# reduce() function takes two arguments, a function and an iterable and returns a single value that is the result of applying the function to the items of the iterable.
# reduce() function is in the functools module, so we need to import it first.
# lambda functions are used in sorting algorithms like sorted(), sort() etc.
sum = lambda a, b: a + b
print(sum(5, 10))
print((lambda x,y:x/y)(10, 5)) #immediate invoked function
# lambda function with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
# lambda function with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
num=map(lambda x:x*2,numbers)
print(list(num))

# decorators
# defination of decorator function is a function that takes another function as an argument, adds some functionality and returns another function.
# decorators are used to modify the behavior of a function without changing its code.
# @ is used to apply a decorator to a function.
# syntax:
# @decorator_function
# def function_to_be_decorated():
#     pass


def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function()
    return wrapper_function
@decorator_function
def display():
    print('display function executed')
display()
# display=decorator_function(display)
# display()
print(type(display))


def decorator_f(f):
    print('decorator function executed')
    def wrapper_f():
        print('wrapper function executed')
        return f()
    return wrapper_f
@decorator_f
def hello():
    print('hello function executed')
hello()
# hello=decorator_f(hello)

def add(f):
    def wrapper(a,b):
        print('addition is:',a+b)
        return f(a,b)
    return wrapper
@add
def mul(a,b):
    print('multiplication is:',a*b)
mul(5,10)
# mul=add(mul)

def calculator(fun):
    def wapper(x,y):
        def add(x,y):
            return x+y
        def sub(x,y):
            return x-y
        def mul(x,y):
            return x*y
        def div(x,y):
            return x/y
        
        return fun(x,y),add(x,y),sub(x,y),mul(x,y),div(x,y)
    return wapper
@calculator
def cal(x,y):
    return x-y
print(cal(10,20))


# decorator calculate function excution time
import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"⏱️ Running '{func.__name__}'...")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"✅ '{func.__name__}' finished in {end - start:.4f} seconds\n")
        return result
    return wrapper


@time_logger
def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total


@time_logger
def slow_function():
    time.sleep(2)
    return "Done sleeping!"


# --- Main Program ---
print("Sum:", calculate_sum(10000000))
print(slow_function())
