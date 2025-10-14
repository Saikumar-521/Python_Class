'''
dict
'''
s=set()
print(type(s))
d={}
print(type(d))
d1={1:'sai',2:22}
print(d1[1])
d1[3]=9346081141
print(d1)

# traverse through dict
for i in d1:
    print(i)
for i in d1:
    print(d1[i])

#dict creation using list of tuple
l1=[(1,'sai'),(2,'kumar'),(3,'sai ram'),(4,'deva')]
d2=dict(l1)
print(d2)

#dict creation using zipmethod: and which is iterable through only iterable data type like list 
l2=['one','two','three','four','five']
d3=dict(zip(l2,l1))
print(d3)

# dict creation using enumarate
l2=['ace','two','threes']
d4=dict(enumerate(l2,start=100))
print(d4,'enumarate')

'''
l1=[x for x in iterable]
t1=(*(x for x in iterable))
s1={x for x in iterable}

'''
# dict creation using compression
d5={key:value for key,value in l1}
print(d5)

d6={x:y for x,y in zip(l2,l1)}
print(d6)

d7={x:y for x,y in enumerate(l2,start=143)}
print(d7)

# methods in dict
d={1:'one',2:'two',3:'three',4:'four'}
print(d)
k=d.keys()
print(k) #dict_keys([1, 2, 3, 4])
v=d.values()
for i in v:
    print(i)

item=d.items()
for i in item:
    print(i)


l3=[1,2,3,4,5]
k=dict.fromkeys(l3)
print(k)

# remove from dict
print(d)
removed_item=d.pop(4)
print(d)
print(removed_item)

d.popitem()
print(d)

d.clear()
print(d)

del d
# print(d)   output is NameError: name 'd' is not defined. Did you mean: 'd1'?