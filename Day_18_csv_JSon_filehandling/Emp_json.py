'''
json module in Python is used for parsing JSON (JavaScript Object Notation) data.
 It allows you to convert between JSON strings and Python objects, making it easy to work with JSON data in your Python programs.
Some common uses of the json module include:
1. Parsing JSON data: You can use the json.loads() function to parse a JSON string
    and convert it into a Python object, such as a dictionary or a list.
2. Generating JSON data: You can use the json.dumps() function to convert a Python object into a JSON string.
3. Reading and writing JSON files: You can use the json.load() and json.dump() functions to read and write JSON data to and from files.
methods(json module):
1. json.load(): This method is used to read JSON data from a file and convert it into a Python object.
2. json.loads(): This method is used to parse a JSON string and convert it into a Python object.
3. json.dump(): This method is used to write a Python object as JSON data to a file.
4. json.dumps(): This method is used to convert a Python object into a JSON string.
5. json.JSONDecoder: This class is used to decode JSON data into Python objects.
6. json.JSONEncoder: This class is used to encode Python objects into JSON data.
7. json.JSONDecodeError: This exception is raised when there is an error in decoding JSON data.
8. json.JSONScanner: This class is used to create a JSON scanner object that can be used to scan JSON data for specific patterns.
import csv
import os
import json
os.chdir('C:\\Users\\G SAIKUMAR\\Desktop\\Python_Class')
with open('dummyJSON.json','r') as file:
    d=json.load(file)
    # print(d)
    for i in d:
        print(i)
        for j in i:
            print(j,':',i[j])
d1={'name':'sai','age':22,'salary':33000}
with open('dummyJSON.json','w') as file:
    json.dump(d1,file)
with open('dummyJSON.json','r') as file:    
    d=json.load(file)
    print(d)
    print(type(d))
print(json.loads('{"name": "sai", "age": 22, "salary": 33000}'))
print(dir(json))
'''
import json
import os

os.chdir('C:\\Users\\G SAIKUMAR\\Desktop\\Python_Class')
# with open('dummyJSON.json','r') as file:
#     d=json.load(file)
#     # print(d)
#     for i in d:
#         print(i)
#         for j in i:
#             print(j,':',i[j])

d1={'name':'sai','age':22,'salary':33000}
with open('dummyJSON.json','w') as file:
    json.dump(d1,file)
with open('dummyJSON.json','r') as file:
    d=json.load(file)
    print(d)

# dump and dumps
data=[1,2,3,4,56,7]
s=json.dumps(data)
print(json.loads(s))



# load and loads
with open('dummyJSON.json','r') as file:
    d=json.load(file)
    print(d)
    print(type(d))

print(json.loads('{"name": "sai", "age": 22, "salary": 33000}'))

print(dir(json))