l1=[1,2,3,4,5]
l2=[1.2,2.3,3.4]
l3=[10+3j,10+1j]
l4=['sai','kumar','anis','ravi']
l5=[1,2,'sai',5.6666,10+1j,True]
# list is define in two ways
# litrial way li=[]
# method way->list()
# list():
# A list can be defined as a collection of values or items of different types.
#  The items in the list are separatedwith the comma (,) and enclosed with the square brackets []
# List is a collection which is ordered and changeable. Allows duplicate members. Lists are objects. 
# There aremany methods associated to them.A list is a sequential collection of Python data values, 
# where each value is identified by an index. The valuesthat make up a list are called its elements

# by using litrial way-->[]
l=[1,2,3.44,5.33,'sai']
print(l)
print(type(l))

# by using list method()
''' list=list(1,2,4.9999,'sai',[1,2,3,4,5,'inner list'])
list=list(1)
print(list)   here list is take oly iterable type like (string ,list,tuple and anges into list) and directly the list can't take integer values
print(type(list))'''

my_list = list((1, 2, 4.9999, 'sai', [1, 2, 3, 4, 5, 'inner list']))
print(my_list)
print(type(my_list))

# repetation (*)
l1=['sai ram','sai ram']
print(l1*3)

# contactination or add
l2=[1,2,3,4,5]
print(id(l2))
print(f'l2 is {l2}')
l2 +=[6,7,8]  #list contatination
print(l2)
print(id(l2))

# Slicing means extracting a portion (sub-list) of a list by using index ranges.
# In Python, slicing is done using the syntax:
# list[start : stop : step]
my_list = [10, 20, 30, 40, 50, 60, 70]
print(my_list[3:20])  #but here the index out of range is not occured in slice,why beacuse the slice end is ened at list last index only
# print(my_list[9])  here error is raise,list index out of range
print(my_list[:0])  #this mean list is empty
my_list[:0]=['first','second']
print(my_list)
# omitting start or stop
print(my_list[:5])
print(my_list[3:])
# using step 
print(my_list[::2])
print(my_list[1::2])

# negative indices
print(my_list[:-1]) #print all elementsin list
print(my_list[-1:]) #print only last element in list
print(my_list[-5:]) #[30, 40, 50, 60, 70]
print(my_list[::-2]) #print in reverse and with step 2,[70, 50, 30, 10, 'first']

'''
| Syntax        | Meaning                               |
| ------------- | ------------------------------------- |
| `list[a:b]`   | Elements from index `a` to `b-1`      |
| `list[:b]`    | From start to `b-1`                   |
| `list[a:]`    | From `a` to end                       |
| `list[a:b:c]` | From `a` to `b-1`, skipping `c` steps |
| `list[::-1]`  | Reverse list                          |

'''

# by using slice add element into the list
my_list[2:4]=['by using slice','method add this two items']
print(my_list)

new_list=[1,2,3,4,5,6,7]
# list methods:

# append(x)
# Add a single element x to the end of the list.
print(new_list)
# print(new_list.append('new element by using append')) when the append method is used direclty in print statement it nothing will print and ,output is None
new_list.append('new element by using append')
print(new_list)

# extend(iterable):
# Add multiple elements from another iterable (list, tuple, etc.).
iterable='SAI'
new_list.extend(iterable)
print(new_list)  #op is, [1, 2, 3, 4, 5, 6, 7, 'new element by using append', 'S', 'A', 'I']

# insert(index,new item)
# this method add the element at particular position
new_list.insert(0,'i am added from insert method at position zero')
print(new_list)

# remove(x)
# Remove the first occurrence of value x. (Error if not found).
new_list.remove('i am added from insert method at position zero')
print(new_list)

new_list.remove(7)
print(new_list)


# pop([i])
# Remove and return element at index i. If no index, removes the last element.
pop_el=new_list.pop() #removes at end of the list
print(new_list)
pop_el += new_list.pop(7)
print(new_list)
print(pop_el)


# index()
# returns the index of the first occurence of value x.
nums = [10, 20, 30, 20]
print(nums)
re_value=nums.index(20)      # 1
print(nums,re_value)
re_value1=nums.index(20, 2)   # 3 it returns the second occurences of 20 element is in 3 indices
print(nums,re_value1)

# count(x)
# Return how many times x appears.
nums = [1, 2, 2, 3]
# nums.count(2)   # 2
print(nums)
print(nums.count(2))


# sort(key=none,reverse=true)
# Sort the list in place.

number=[2,320,40,55,46,90,65]
number.sort()
print(number)
number.sort(reverse=True)
print(number)

# reverse()
# Reverse the list in place.
number.reverse()
print(number)

print(number[::-1])

'''
| Method                          | Definition                                       |
| ------------------------------- | ------------------------------------------------ |
| `append(x)`                     | Add `x` to the end                               |
| `extend(iterable)`              | Add all elements from iterable                   |
| `insert(i, x)`                  | Insert `x` at index `i`                          |
| `remove(x)`                     | Remove first occurrence of `x`                   |
| `pop([i])`                      | Remove & return item at index `i` (default last) |
| `clear()`                       | Remove all items                                 |
| `index(x[, start[, end]])`      | Return index of `x`                              |
| `count(x)`                      | Count occurrences of `x`                         |
| `sort(key=None, reverse=False)` | Sort list in place                               |
| `reverse()`                     | Reverse list in place                            |
| `copy()`                        | Shallow copy of list                             |

'''