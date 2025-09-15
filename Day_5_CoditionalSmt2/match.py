'''
match:
The match statement was introduced in Python 3.10.
It is similar to a switch-case statement in other languages (like C, Java, JavaScript).
It allows you to compare a variable (or expression) against different patterns and run code depending on the match.

syntax:
match variable:
    case pattern1:
        # code block
    case pattern2:
        # code block
    case _:
        # default case (like "else")



'''
day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")

service =input('deposit, witdraw, checkBal')
bal=500
match service:
    case 'deposit':
        amount=int(input('enter amount'))
        bal +=amount
        print(bal,'deposited sucessfully')
    case 'withdraw':
        amount=int(input('enter amount to with draw'))
        bal -=amount
        print(bal,'available balance')
    case 'checkBal':
        print(bal,'the balance')
    case _:
        print('select service')

