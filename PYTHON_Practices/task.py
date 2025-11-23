def iseven(num):
    if num%2==0:
        print('given number is even',num)
    else:
        print('given number is odd',num)

iseven(5)
iseven(4)

def isprime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        print('it is prime number')
    else:
        print('it is not a prime number')

isprime(2)
isprime(4)

def factorial(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    print(f)

# for i in range(1,11):
    factorial(i)

def findfactor(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i,'is the factor of ',num)

findfactor(9)
    