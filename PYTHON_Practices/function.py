import random
otp=random.randint(10,20)
print(otp)
c=1
mark=20
n=4
while n>0:
    user=int(input('enter a number'))
    if otp==user:
        print('successfully matched')
        break
    else:
        print('pls enter a number correctly and you have',n-1,'time chances only')
        c=c+1
    n=n-1
c=c-1
if c==4:
    print('you lost the game, and your score is zero')
elif c>0:
    c=c-1
    print('you scored',mark/c)

import userdefined as ud

x=20
y=10
print(ud.add(x,y))
print(ud.sub(x,y))
print(ud.mul(x,y))
print(ud.div(x,y))
print(ud.isprime(x))