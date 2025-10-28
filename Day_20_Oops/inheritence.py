'''
inheritence:
'''
'''


class A:
    def feature1(self):
        print('feature 1 working')

    def feature2(self):
        print('feature 2 working')
    
class B(A): #single level inheritance
    def feature3(self):
        print('feature 3 working')

    def feature4(self):
        print('feature 4 working')
    
class C(B): # multi level inheritance
    def feature5(self):
        print('feature 5 working')

    def feature5(self):
        print('feature 6 working')
    

a1=A()
a1.feature1()
a1.feature2()
print('single level inheritance')
b=B()
b.feature3()
b.feature4()
b.feature1()
b.feature2()
print('multi level inheritance')
c=C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
    


'''

'''
class A:
    def feature1(self):
        print('feature 1 working')

    def feature2(self):
        print('feature 2 working')
    
class B: #
    def feature3(self):
        print('feature 3 working')

    def feature4(self):
        print('feature 4 working')
    
class C(A,B): # multple inheritance
    def feature5(self):
        print('feature 5 working')

    def feature5(self):
        print('feature 6 working')
    

a1=A()
a1.feature1()
a1.feature2()
print('single level inheritance')
b=B()
b.feature3()
b.feature4()
# b.feature1() here class B not inheritance the properites from class A so we can't access
# b.feature2()
print('multi level inheritance')
c=C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
   ''' 

# constructor in inheritance how it behaves
# MRO(method resolution order)
'''
class A:

    def __init__(self):
        print('in A init')


    def feature1(self):
        print('feature 1 working')

    def feature2(self):
        print('feature 2 working')
    
class B(A): 

    def __init__(self):
        super().__init__()
        print('in B init')

    def feature3(self):
        print('feature 3 working')

    def feature4(self):
        print('feature 4 working')

a=B()
# a.feature1() before using the super keyword the feature1 method is inherit

# if you create object of sub class it will first try find init of sub class,if it is not found then it will call init of super class
# solution:
# then we use super()._init_()

'''

class A:

    def __init__(self):
        print('in A init')


    def feature1(self):
        print('feature 1 working')

    def feature2(self):
        print('feature 2 working')
    
class B: 

    def __init__(self):
        # super().__init__()
        print('in B init')

    def feature3(self):
        print('feature 3 working')

    def feature4(self):
        print('feature 4 working')
class C(A,B):
    def __init__(self):
        super().__init__() #here init is from A class the B class is not getting,for we have the MRO(method resolution order),by default it is from left to rigth
        print('c init')
    # def feat(self):
        # super.feature3()
c=C()
# c.__init__() # it will get the only c Class init method
# c.feat()

