'''
poly---many
morhism---forms

types of polymorphism
1.duck typing
2.operator overloading
3.method overloading
4.method overriding
'''
# duck typing
class pycham:
    def excute(self):
        print('compling')
        print('running ')
class Myeditor:
    def excute(self):
        print('spell check')
        print('convention check')

class laptop:
    def code(self,ide):
        ide.excute()
    
l=laptop()
pycham_obj=pycham()
myeditor=Myeditor()

l.code(pycham_obj)
l.code(myeditor)


# operator overloading
# in python there is no implicity conversion
a=4
b='hello'
# print(a+b) TypeError: unsupported operand type(s) for +: 'int' and 'str',
a=5
b=6
print(a+b)
print(int.__add__(a,b))

# print(str.__add__(a,b)) TypeError: descriptor '__add__' requires a 'str' object but received a 'int'

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,others):
        m1=self.m1+others.m1
        m2=self.m2+others.m2
        s3=student(m1,m2)

        return s3


s1=student(23,45)
s2=student(40,60)
# s3=s1+s2 TypeError: unsupported operand type(s) for +: 'student' and 'student'

# s3=s1+s2  ->student.__add__(s1,s2)
s3=s1+s2
print(s3.m1)
print(s3.m2)

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,others):
        m1=self.m1+others.m1
        m2=self.m2+others.m2
        s3=student(m1,m2)
        return s3
    def __gt__(self,other):
        r1=self.m1 + self.m2
        r2=other.m1 + other.m2
        if r1>r2:
            return True
        else:
            return False
    # def __str__(self):
    #     return 


s1=student(23,45)
s2=student(40,60)
s3=s1+s2
print(s3.m1)

if s1>s2:
    print('s1 win')
else:
    print('s2 is win')


# method overloading
class student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def sum(self,a=None,b=None,c=None): #even if we don't pass the parameter than  TypeError: student.sum() missing 1 required positional argument: 'c' was not genrated
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
s1=student(50,60)
print(s1.sum(4))

# method overriding
class A:
    def show(self):
        print('in A show')

# class B(A):
#     pass
class B(A):
    def show(self):
        print('B Show')


a1=B()
a1.show()
    