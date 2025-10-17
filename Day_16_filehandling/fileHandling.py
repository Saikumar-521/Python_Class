# file=open('test.txt','r')
# f=file.read(30)
# print(f)
# file.close()

# f=open('test1.txt','w')
# f.write('Hi, hello world')
# f.writelines('''
# this is my first file handling
#               i want to create some
#                  text file
# ''')
# f.close()

# file=open('test1.txt','r')
# print(file.read(1))

# file=open('test1.txt','r+')
# l=file.read()
# file.write(l)
# file.close()

# fname=input('enter file name')
# nolin=0
# nowords=0
# nochar=0
# fn=open(fname,'r+')
# for i in fn:
#     words=i.split()
#     nowords+=len(words)
#     nochar +=len(i)
#     nolin+=1
# print('number of lines',nolin)
# print('number of words',nowords)
# print('number of character',nochar)
# import csv
# p=[('sai',22,33),('kumar',20,24),('tej',32,34)]
# csvf=open('p.csv','w',newline=' ')
# obj=csv.writer(csvf)
# for person in p:
#     obj.writerow(person)

# csvf.close()

import json
data=[1,2,3,4,56,7]
s=json.dumps(data)
print(json.loads(s))
print(dir(json))