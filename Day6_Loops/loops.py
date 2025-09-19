'''conditional loops
while sentinal
for--->for each loop

while:
A while loop is used to repeat a block of code as long as a condition is True.
When the condition becomes False, the loop stops.

syntax:

while conditon:
  #block of code

for 
A for loop is used to iterate over a sequence (like a list, string, tuple, dictionary, or range of numbers).
It repeats the code block for each element in that sequence.

syntax:
for variable in sequence:
    # code block

range(start,stop,step)
range(10)--------->it is the stop value
range(1,10)----->1 is the start value and 10 is the stop value
by default the value of start is (0) and step is 1
'''

# while loop
# num=int(input("enter number"))
# while num<100:
#     if num%2==0:
#         print("this number is even",num)
#     num +=1

# n=int(input('enter number'))
# c=0
# while n>0:
#     n=n//10
#     c +=1
# print(c)

# n=int(input("enter number"))
# copy=n
# rev=0
# while n>0:
#     x=n%10
#     print(x,end=" ")
#     rev=rev*10+x
#     n//=10
# print(rev)
# if rev==copy:
#     print("is palindrome number")
# else:
#     print("is not a palindrome number")

'''for loop'''
#printing string charaters
# name="sai kumar"
# for i in name:
#     print(i,end=' ')

# reverse a string
# text=input('enter a string')
# print('reverse of string',text[::-1])

# reverse a string based on space
# words = text.split(" ")
# reversed_words = [word[::-1] for word in words]
# reversed_each_word = " ".join(reversed_words)
# print(reversed_each_word)

# factorial of number
n=int(input('enter number to know factorial of the number'))
fact=1
for i in range(1,n+1):
    fact *=i
print("Factorial of ",n," is: ",fact)

# using recursion
def fact(n):
    if n==0 or n==1:
        return n
    else:
        return n*fact(n-1)
print(f'using recursion  factorial of {n} is the {fact(n)}')

# factors of a number
def factor(n):
    r=[]
    for i in range(1,n+1):
       if n%i==0:
          r.append(i)
    return r
print(f'the factors of {n} is {factor(n)}')

# prime number program
for i in range(1,n+1):
    c=0
    for j in range(1,n+1):
        if i%j==0:
            c+=1
    if c==2:
        print("is a prime number",i)
    else:
        print("is not a prime number",i)

for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(" * ",end=' ')
    print()

for i in range(1,n+1):
    for j in range(n+1):
        if i<=j:
            print(" * ",end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i>j or j>i:
            print(" * ",end=' ')
    print()

for i in range(n):
    for j in range(n-i-1):
        print("*",end='')
    print()

for i in range(n):
    print("*" * (n - i - 1))

# |  i | `range(n - i - 1)` expands to | stars printed this row |
# | -: | ----------------------------: | :--------------------- |
# |  0 |      `range(4)` → j = 0,1,2,3 | `****`                 |
# |  1 |        `range(3)` → j = 0,1,2 | `***`                  |
# |  2 |          `range(2)` → j = 0,1 | `**`                   |
# |  3 |            `range(1)` → j = 0 | `*`                    |
# |  4 |  `range(0)` → (no iterations) |  (empty line)      |



for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))

for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))


# ANSI escape codes
print("\033[31mThis is Red\033[0m")
print("\033[32mThis is Green\033[0m")
print("\033[33mThis is Yellow\033[0m")
print("\033[34mThis is Blue\033[0m")


# jumping statements in python
# 1.break
# Used to terminate the loop immediately, even if the loop condition is still true.
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# continue
# Skips the current iteration and moves to the next one.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# pass
# A null statement (does nothing).
# Used as a placeholder when code is syntactically required but you don’t want to execute anything yet.



# assert
# The assert keyword in Python is used for debugging and testing. 
# It helps check if a condition is True while your program is running.
# If the condition is False, it raises an AssertionError (optionally with a message).
# synatx: assert condition, message

x = 10
assert x > 0
print("x is positive")
