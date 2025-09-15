import math
'''
1.pythom is a hidh level programming language and its versantality and python is the dynamic typed language,the python is the interpreter
language which means excutes the the code line by line,it have more applications
1.dynamic typed laguage
2.OOPs
3.reach modules
'''
print('Welcome to python programming')

'''
3.conversion
conversion means converting one datatype into the another datatype
1.implicit conversion
implicit conversion can done automatically,the datatype converting from smaller to larger dataype
a=10
b=7
print(a/b)

2.explicit conversion
explicit conversion can do developers/programmers,converting large datatype into lower datatype,
a=10
print(a)
print(type(a))
a=float(a)
print(type(a))

'''
a=25
print("int to binary: ",bin(a))
print("int to oct: ",oct(a))
print('int to hex',hex(a))

s='1234'
print(type(s))
s=int(s)
print(type(s))
print(s)
#operators & expressions

# a=float(input('enter a number'))
# b=float(input('enter b number'))
# c=float(input('enter c number'))

# d=b**2-4*a*c
# r1=(-b+math.sqrt(d))/(2*a)
# r2=(-b-math.sqrt(d))/(2*a)
# print(r1,r2)




user=int(input('Enter number'))
if user%3==0 and user%5==0 and user%10 !=0:
    print(user,"this number divisible by both 3 and 5")


#conditional statements
year=int(input('enter year'))
if year%400==0:
    print(year,'is a leap year')
elif year%100!=0 and year%4==0:
    print(year,'is aleap year')
else:
    print(year,'not a leap year')

a,b,c=1,2,3
if a>b and a>c:
    print(a,"is gretest value")
elif b>a and b>c:
    print(b,'is greatest value')
else:
    print(c,'is the greatest value')

marks=int(input('enter marks'))
if marks>=90:
    print('Excellent')
elif marks>=75:
    print('Good')
elif marks>=50:
    print('Average')
else:
    print("Fail")

num=int(input('enter number'))
i=1
while i<=10:
    print(num,'*',i,'=',num*i)
    i+=1


a=1
while a<=5:
    print(end="")
    i=1
    while i<=a:
        print('*')
        i+=1
    print()
    a+=1



number=1
while number<=100:
    print('the factorial of',number)
    fact=1
    while fact<=number:
        if number%fact==0:
            print(fact)
        fact=fact+1
    print()
    number=number+1


