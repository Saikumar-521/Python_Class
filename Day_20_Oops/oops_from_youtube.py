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
   f.abstraction: hiding the essitinal data
4. advantages of OOPs:
   a. code reusability: classes can be reused in different parts of the program or in different programs
   b. modularity: code can be organized into smaller, more manageable pieces
    c. maintainability: code can be easier to maintain and update
    d. flexibility: objects can be easily modified or extended without affecting other parts of the program
5. popular OOPs languages: Python, Java, C++, Ruby, etc.






class:
class is a collection of object,A class contains the blueprint or prototype form which
objects are beging created,
it is a logical entity that contains attributes and methods.

object:
an object in python is an instance of a class,
that contains data(attribues) and functions(methods)
which define its behavior,
the object is pyhsical entity that has state and behavior,

init:
the __init__ method in python is a special method
and also called a constructor that is automatically called
when a new object of a class is created.
**it is used to to initialize the attributes (data) of the object

***** __init__ sets the initial state of an object

Can take additional parameters to initialize attributes.
Does not return anything (return is implicit None).



self: in short it describes is self refers to the current object itself(for underatanding)

self is a conventionally named parameter in Python that represents the instance (object) of the class.
It allows access to the attributes and methods of the object within the class.


instance variable:
Instance variables are variables that are defined inside a class 
but belong to each object (instance) of that class.
Each object has its own copy of the instance variables, 
so changes to one object’s variables do not affect others.

In short:
Instance variables store data that is unique to each object.
key points:
Defined inside __init__ or other instance methods using self.
Belong to the object, not the class.
Can be accessed or modified using object references.


class variable:
A class variable is a variable that is shared among all instances (objects) of a class.
It is defined inside the class but outside any instance method,
 and its value is common to all objects of that class.

In short:
Class variables store data that is shared by all objects of a class.

Key Points:
Defined inside the class but outside __init__ or any method.
Shared across all objects.
Can be accessed using class name or object.
Useful for storing constants or shared data.

constuctor:
A constructor in Python is a special method of a class that is automatically called when a new object is created.
Its purpose is to initialize the object’s attributes and set up its initial state.


types of methods:

instance method(self):
An instance method is a function defined inside a class that operates on an instance (object) of the class.
It can access and modify the attributes of the object using the self parameter.

@class methods
class method(cls):
A class method is a method that is bound to the class rather than its objects.
It can access and modify class-level attributes (shared by all instances) and is defined using the @classmethod decorator.
Its first parameter is conventionally cls, which refers to the class itself, not the instance.

@staticmethod
static method():
A static method is a method that belongs to a class rather than any specific object.
It does not have access to instance (self) or class (cls) variables.
It is defined using the @staticmethod decorator.

or
in short

Static method = a utility function inside a class that works
 independently of objects and class state.

'''
# from os import name
# from traceback import print_tb
# from sympy import true


class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        # return 'ram' init method can't return any thing but impciltly it returns None
 #self is the object
#  each object have its own value
    def config(self):
        print('Config is',self.cpu,self.ram)
        # print('model of computer',model)
    def company(self,name):
        print(self.cpu,self.ram)
        print(name)

com1=Computer('i5',16)  #creating object one that is com1
com2=Computer('ryzen',6) #creating object second that is com2

Computer.config(com1)  #calling the instance method by using method of object
Computer.config(com2)

com1.config() #calling the config method by using the object
com2.config() 

# sending arugments to the company method
Computer.config(com1)
Computer.company(com1,'dell')

com1.company('sai')
print(id(com1))
print(id(com1.company))
print(id(com2))
print(id(com2.company))
# methods address in the class is all same
'''
constructor
self:self refering to the object and current instance
and
comparing objects in python



'''
class com:
    def __init__(self):
        self.name='sai'
        self.age=22
    def update(self):
        self.age=16
    
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False



c1=com()
# print(id(c1)) 2263777899392
c2=com()
# print(id(c2))  2263779201808
# all objects are created in heap memory

print('printing the same name when we call the different objects')
print(c1.name,'and',c1.age)
print(c2.name,'and',c2.age)

if c1.compare(c2):
    print('yes they are same')

c2.update()
print('after updation of age')
if c1.age==c2.age:
    print('they are same')
else:
    print('they are not same')

# now change the name of object2
c2.name='sameera'
print(c2.name)
# c2.update()

'''
size of object is based on the number of variable avaliable in methods
'''

# ---------------------------------------------------------------------------------------------------------------
# types of variables in python
# instance variables: if we define the variables inside the init method those are the instance variables
# class variables or static variables: if we define the variables inside the class and outside of __init__ method those are class or static variables
'''
namespace is an area where you create and stroe object/ variable
class namespace: class variables create in class namespace
object/instance namespace
'''
class car:
    wheels=4

    def __init__(self):
        # these are the instance variables
        self.mil=10
        self.com='tata'

c1=car()
print(f'object one c1 wheels {c1.wheels}')
c2=car()
print(f'prints object two c2 wheels {c2.wheels}')
c1.mil=10
print(c1.com,c1.wheels,c1.mil)
c2.com='bmw'
print(c2.com,c2.mil,c2.wheels)


# ----------------------------------------------------------------------------------------------------------
# in variables the class and static both are same but in methods class method and static methods are different
'''
instance methods
class methods
static methods: if we don't concerned with class variable and instance variable ,and if we want extra functionality without the class and instance variable is know static variable
'''

class student:
    school='zphs'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self): #instance method
        return (self.m1+self.m2+self.m3)/3
    # if we work with the instance variable use self
    # if we work with the class variable use cls
    @classmethod
    def getschool(cls): #class method
        return cls.school
    
    @staticmethod
    def info(): #static method
        print('this is student class....in abc module')

s1=student(23,45,67)
s2=student(56,78,98)
res=s1.avg()
print(res)
print(s2.avg())

print('printing class variables using class methods')
# print(student.info()) TypeError: student.info() missing 1 required positional argument: 'cls'---------------with out using @classmethod decorator
print(student.getschool()) #class method is accessing through the class of m

# static method
student.info()
# ------------------------------------------------------------------------------------------------
# class inside a class
# for inner class,we are createing object in two ways
# inside the outter class of init method
# outside the outter class using the outter class object
class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=4
        def show(self):
            print(self.brand,self.cpu,self.ram)
        
s1=student('sai',21)
s2=student('kalyan',23)
# print(s1.name,s1.rollno)
# print(s2.name,s2.rollno)
s1.show()
s2.show()

# s1.lap.brand
# lap1=s1.lap
# lap2=s2.lap
# print(id(lap1))
# print(id(lap2))

lap1=student.Laptop()
lap1.show()

'''
difference between the accessing of instance and class variables
✅ Summary:
Method Type	      Can access instance variables?	Can access class variables?
Instance method	  ✅ Yes (via self)	              ✅ Yes (via self or class)
Class method	  ❌ No (unless object passed)	  ✅ Yes (via cls)
Static method	  ❌ No	                          ✅ Only via class name

'''
