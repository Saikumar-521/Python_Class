'''

'''
# from os import name


class student:
    school='ZPHS Nangnoor'
    def __init__(self,name,rollno):
        self.name=name  #instance variables
        self.rollno=rollno
    def marks(self,mark): #instance method
        print(f'name: {self.name} and rollNo {self.rollno} his marks {mark}')
        # print(school) class variables can't access diritecly in the instance variable
        print(student.school) #but access through the class name
        print(self.school) #class variables access through the instance of class
    @classmethod
    def class_method(cls):
        # print(student.class_method())  RecursionError: maximum recursion depth exceeded
        print(student.school) #class attribute/variable are access through class only
        # print(self.school) #TypeError: student.class_method() missing 1 required positional argument: 'self'
    
    @staticmethod
    def static_method():
        print('static method \n',student.school)

s1=student('sai',21)
s1.marks(60) 
print('class method')
s1.class_method()
print('class method can access the class variable through object')
print(s1.school)
print('static method')
s1.static_method()