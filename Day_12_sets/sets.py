'''
set():
In Python, a set is an unordered collection of unique elements.

It means:
Duplicates are not allowed.
Order is not guaranteed (the elements may appear in any order).
Mutable, so you can add or remove elements after creation.
Set elements must be immutable types (like numbers, strings, tuples).
'''
from traceback import print_tb


s={}
print(type(s))  #<class 'dict'>
s={1}
print(type(s))  #<class 'set'>

s1=set()
print(s1)  #set()
d={}
print(d) #{}

s2=set([1,2,3,4,5,6,7,12,3,4,5,6,7])
print(s2)

s3=set('python')
print(s3)

s4={'sai',12,2.34,'pthy'}
print(s4)

for x in s4:
    print(x)

# add()
s5={10,20,30,40,50}
print(s5)
s5.add(60)
print(s5)

# pop(): it will remove any random element
s5.pop()
print(s5)

# remove(): it wil remove specific element
s5.remove(20)
print(s5)


# sets in mathamatics
s1={1,2,3,4,5,6,7,8,9,10}
a={1,2,3,4,5} #here s1 is super set of a
b={6,7,8,9,10}  #here s1 is super set of b
c={1,2,3,4,5,6,7,8,9,10} #here c is properset of s1

# union() (A ∪ B)
# The union of two sets is a set that contains all unique elements from both sets.
# Duplicate elements are removed automatically.
'''
A | B

A.union(B)

'''
print(s1| b)
print(a.union(b))

# intersection (A ∩ B)
# The intersection of two sets is a set that contains only the elements that are common to both sets.
'''
A & B
A.intersection(B)

'''
print(s5 & a)
print(s1.intersection(b))

# difference (a-b)
# The difference of two sets (A - B) is a set containing elements that are in A but not in B.
'''
A - B
A.difference(B)

'''
print(s1-a)
print(s1.difference(b))

# 4. Symmetric Difference (A △ B)
# The symmetric difference of two sets is a set that contains elements that are in either of the sets, but not in both.
'''
A ^ B
A.symmetric_difference(B)

'''

A = {1, 2, 3}
B = {3, 4, 5}
result = A ^ B
print(result)   # Output: {1, 2, 4, 5}


# 5. Subset (A ⊆ B)
# A set A is a subset of B if all elements of A are also present in B.

# Syntax:
# A <= B
# A.issubset(B)

A = {1, 2}
B = {1, 2, 3, 4}
print(A <= B)   # Output: True

A = {1, 2,5}
B = {1, 2, 3, 4}
print(A.issubset(B)) #false

# 6. Superset (A ⊇ B)
# A set A is a superset of B if it contains all elements of B.
# A >= B
# A.issuperset(B)

A = {1, 2, 3, 4}
B = {2, 3}
print(A >= B)   # Output: True

A = {1, 2, 3, 4}
B = {2, 3,5}
print(A >= B) #false



# 7. Disjoint Sets
# Two sets are disjoint if they have no elements in common.
# Syntax:
# A.isdisjoint(B)
A = {1, 2, 3}
B = {4, 5, 6}
print(A.isdisjoint(B))   # Output: True

a={1,2,3}
b={3,4,5,6}
print(a.isdisjoint(b))  #false

input='education'
s=set(input)
vowels='aeiou'
c=0
for x in s:
    if x in vowels:
        c=c+1
print(c)

l1=[1,2,3,4,5,6]
l2=[1,2,3,6,7,8]
s1=set(l1)
s2=set(l2)
print(s1 & s2)

input="Python is easy and Python is powerful"
set=set(input.split())
print(set)


# find first commn element in set
a={1,2,3,4}
b={5,6,7,4,3,2,1}
for i in a:
    for j in b:
        if i==j:
            print(i)
    break