import random
# # password=input('Enter your password')
# no_attemptes=1
# while no_attemptes<=10:
#     password=input('Enter your password')
#     if password=='saikumar123':
#         print('Successfully Login!')
#     else:
#         print('Enter correct Password please')
#     print('you attempte',no_attemptes,'this many times')
#     no_attemptes += no_attemptes

'''pin question'''
# pin=12345
# attempts=3
# while attempts >0:
#     entered=int(input('Enyter PIN:'))

#     if entered==pin:
#         print('Access Granted')
#         break
#     else:
#         attempts -= 1
#         print('Wrong pin attempts left',attempts)
# if attempts==0:
#     print('Account locked')
'''number guessing game'''
# secret =random.randint(1,10)
# guess=0
# while guess != secret:
#     guess=int(input('guess the number'))
#     if guess <secret:
#         print('TOo low')
#     elif guess >secret:
#         print('Too high')
#     else:
#         print('correct')
'''Right angle triangle'''
# for i in range(1,5+1):
#     print("*"*i)
'''Reverse right anle triangle'''
# for i in range(6,0,-1):
#     print("&"*i)
'''pyramid centered trianle & reverse pyramid centered trianle'''
# n=6
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))
# n=6
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))
'''diamond shape'''
# n=6
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))

# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))

n=5
for i in range(n):
    print(" * "*n)

n = 7   # size of S

for i in range(n):
    for j in range(n):
        # Top row
        if i == 0 and j > 0:
            print("*", end=" ")
        # Middle row
        elif i == n//2:
            print("*", end=" ")
        # Bottom row
        elif i == n-1 and j < n-1:
            print("*", end=" ")
        # Left vertical (top half)
        elif i < n//2 and j == 0:
            print("*", end=" ")
        # Right vertical (bottom half)
        elif i > n//2 and j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



n = 7   # height of A

for i in range(n):
    for j in range(n):
        # conditions to draw A
        if (j == 0 or j == n-1) and i != 0:   # left & right side, except top
            print("*", end=" ")
        elif i == 0 and j != 0 and j != n-1:  # top row
            print("*", end=" ")
        elif i == n//2:                       # middle bar of A
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 7   # height/width of I

for i in range(n):
    for j in range(n):
        # Top row
        if i == 0:
            print("*", end=" ")
        # Bottom row
        elif i == n-1:
            print("*", end=" ")
        # Middle column
        elif j == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


'''SAI NAME pattern'''
# ANSI color codes
GREEN = "\033[92m"
RESET = "\033[0m"
RED = "\033[91m"

n = 7   # size of letters

for i in range(n):
    # ---- S ----
    for j in range(n):
        if i == 0 and j > 0:
            print(GREEN + "*" + RESET, end=" ")
        elif i == n//2:
            print(GREEN + "*" + RESET, end=" ")
        elif i == n-1 and j < n-1:
            print(GREEN + "*" + RESET, end=" ")
        elif i < n//2 and j == 0:
            print(GREEN + "*" + RESET, end=" ")
        elif i > n//2 and j == n-1:
            print(GREEN + "*" + RESET, end=" ")
        else:
            print(" ", end=" ")
    print("   ", end="")  # spacing between letters

    # ---- A ----
    for j in range(n):
        if (j == 0 or j == n-1) and i != 0:
            print(GREEN + "*" + RESET, end=" ")
        elif i == 0 and j != 0 and j != n-1:
            print(GREEN + "*" + RESET, end=" ")
        elif i == n//2:
            print(GREEN + "*" + RESET, end=" ")
        else:
            print(" ", end=" ")
    print("   ", end="")  # spacing between letters

    # ---- I ----
    for j in range(n):
        if i == 0:
            print(GREEN + "*" + RESET, end=" ")
        elif i == n-1:
            print(GREEN + "*" + RESET, end=" ")
        elif j == n//2:
            print(GREEN + "*" + RESET, end=" ")
        else:
            print(" ", end=" ")
    print()

    for col in range(7):
        # Upper lobes of heart
        if (i == 0 and col % 3 != 0) or (i == 1 and col % 3 == 0) or (i - col == 2) or (i + col == 8):
            print(RED + "*" + RESET, end=" ")
        else:
            print(" ", end=" ")
    print()

