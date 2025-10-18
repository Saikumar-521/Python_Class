'''
exception handling:
defination: the process of responding to the occurrence, during computation, of exceptions – anomalous or exceptional conditions requiring special processing – 
often changing the normal flow of program execution.

or
exception handling is a programming construct or mechanism designed to handle the occurrence of exceptions,
which are unexpected events or errors that disrupt the normal flow of a program's execution.

try:
    # code that may raise an exception
except SomeException:
    # code that runs if the exception occurs
finally:
    # code that always runs, regardless of whether an exception occurred or not

with else:
    # code that runs if no exception occurs in the try block


'''
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return f"The result is {result}"
    finally:
        print("Execution of divide_numbers is complete.")

print(divide_numbers(10, 2))  # Should print the result
print(divide_numbers(10, 0))  # Should handle division by zero error


'''Output:Execution of divide_numbers is complete.The result is 5.0
Execution of divide_numbers is complete.Error: Division by zero is not allowed.         
'''

# a=int(input('enter a number'))

# if type(a)==int:
#     print(a)
# else:
#     print(a)

# exception handling with file

f='test1.txt'
file=open(f,'w')
file.write('i am from exception handling')
# print(file)
file.close()
file=open(f,'r')
for i in file:
    print(i)
file.close()
# exception handling with file
# f='test.txt'
# try:
#     file=open(f,'r')
#     content=file.read()
#     print(content)
# except FileNotFoundError:
#     print(f"Error: The file '{f}' was not found.")
# else:
#     f=open('test.txt','a')
#     f.write('file found successfully')
# finally:
#     if 'file' in locals():
#         file.close()
#         print("File has been closed.")
filename = 'test.txt'

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    # Create a new file and write an initial message
    with open(filename, 'w') as file:
        file.write('New file created because it was not found.\n')
    print(f"A new file '{filename}' has been created.")
else:
    with open(filename, 'a') as file:
        file.write('\nFile found successfully.')
    print("Message appended successfully.")
finally:
    print("Program completed.")


def add(a,b):
    try:
        return a+b
    except TypeError:
        return "Error: Invalid input types for addition."
    else:
        return a+b         
print(add(5,10))  # Should print 15
print(add(5,'10'))  # Should handle type error


def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: Index out of range."
    except TypeError:
        return "Error: Invalid index type."
    else:
        return lst[index]   
print(access_list_element([1, 2, 3], 1))  # Should print 2
print(access_list_element([1, 2, 3], 5))  # Should handle index error
print(access_list_element([1, 2, 3], 'a'))  # Should handle type error


def division(a,b):
    try:
        return a/b
    except Exception as e:
        return f"An error occurred: {e}"
    # else:
    #     return a/b
    finally:
        print("Division operation attempted.")
print(division(10, 2))  # Should print 5.0
print(division(10, 0))  # Should handle division by zero error

