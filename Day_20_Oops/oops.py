'''
paradigm:
paradigm is a way of thinking about programming
there are many programming paradigms

or 
paradigm is defined as a model or pattern of something 


A paradigm means a model, pattern, or way of thinking about something.
So, in simple words:
A programming paradigm is a style or approach to writing and organizing code.
It defines how you think about problems and how you structure your programs.


OOPs
object oriented programming:
1. it is a programming paradigm that uses "objects" to design software.
2. it is used to structure a software program into simple, reusable pieces of code blueprints
3. it is based on several key concepts including:
   a. class: a blueprint for creating objects
   b. object: an instance of a class
   c. inheritance: a mechanism for creating a new class from an existing class
   d. polymorphism: the ability of different classes to be treated as instances of the same class through a common interface
   e. encapsulation: the practice of hiding the internal details of an object and exposing only the necessary parts
4. advantages of OOPs:
   a. code reusability: classes can be reused in different parts of the program or in different programs
   b. modularity: code can be organized into smaller, more manageable pieces
    c. maintainability: code can be easier to maintain and update
    d. flexibility: objects can be easily modified or extended without affecting other parts of the program
5. popular OOPs languages: Python, Java, C++, Ruby, etc.


1.class :class is combination of group of variables and group of methods
2.object :
3.encapsulation
4.inheritance(types)
5.abstraction(acess spacifers)
6.polymorphrism(method overloading, methodoveriding)---->poly----means--many,morphrism--->means--forms


syntax:
class className:
   //class variables
   def __init__(self,parameter):
        parameters variable declaration
        //instance variables
    
    def add(self,a,b):
       a+b

a=className() #object creation
a.add(10,20)


class variables vs instance variables
class Car:
    # class variable
    wheels = 4

    # constructor
    def __init__(self, make, model):
        # instance variables
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.make} {self.model} has {Car.wheels} wheels."
car1 = Car("Toyota", "Camry")
car1.display_info()  # Output: Toyota Camry has 4 wheels.
car2 = Car("Honda", "Civic")
'''

from operator import ge


class Person:
    gender='male'  #class variable
    def __init__(self,name,age):  #instance variable
        self.name=name
        self.age=age
    def display(self):   #instance method
        return f"Name:{self.name}, Age:{self.age} and Gender is:{Person.gender}"
male=Person('sai',22)
# print(male.display('sai',22,'male')) Person.display() takes 3 positional arguments but 4 were given
print(male.display())

# passing parameters to instance method
class Person:
    gender='male'  #class variable
    def __init__(self,name,age):  #instance variable
        self.name=name
        self.age=age
    def display(self):   #instance method
        return f"Name:{self.name}, Age:{self.age} and Gender:{Person.gender}"
male=Person('sai',22)
print(male.display())
# print(Person.display(male)) #Name:sai, Age:22 and Gender:male
# print(Person.display()) #missing 1 required positional argument: 'self'
# print(Person.display('sai',22)) #Person.display() takes 1 positional argument but 3 were given 
print(Person.display('sai')) #Person.display() takes 1 positional argument but 2 were given