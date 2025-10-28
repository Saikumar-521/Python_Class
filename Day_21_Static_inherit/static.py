'''
static methods()
'''
# from textdistance import length


class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)
    
    @staticmethod
    def perameter(length,breath):
        print(2*length*breath)
    
    def space():
        print('static methods ')
    
rec=Rectangle(2,3)
rec.area()
# rec.perameter(10,20) #TypeError: Rectangle.perameter() takes 2 positional arguments but 3 were given
Rectangle.perameter(10,20) #static methods use the @StaticMethods
Rectangle.space() 

'''
inhertences:

'''

class Parent:
    def __init__(self):
        pass
    def display(self):
        print('This is aparent class')

class Child(Parent): #inherit from parent
    def __init__(self):
        super().__init__()

    def show(self):
        print('this is a child class')

child=Child()
child.display()
child.show()
# print(Child.display) #This is aparent class
# print(Child.show) #this is a child class
print(child.display()) #output None

'''
basic
multiple
multilevel
hirarical
'''

class Daddy:
    def skill(self):
        print('He is a good business man')

class Mommy:
    def talent(self):
        print('she is a singer')
class son(Daddy,Mommy):
    def own(self):
        print('good fellow')

s=son()
s.skill()
s.talent()
s.own()
        
