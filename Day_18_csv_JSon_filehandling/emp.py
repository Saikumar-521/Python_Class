'''
csv file handling
definition: csv file handling is a way to store data in a tabular format, where each row represents a record and each column represents a field. 
CSV files are commonly used for data exchange between different applications and platforms.
method:
1. importing the csv module: The first step in handling CSV files is to import the csv module in Python. This module provides functions for reading and writing CSV files.
2. reading CSV files: To read a CSV file, you can use the csv.reader() function, which returns an iterable object that can be used to iterate over the rows in the file.
3. writing CSV files: To write data to a CSV file, you can use the csv.writer() function, which returns a writer object that can be used to write rows to the file.
4. working with CSV files using pandas: The pandas library provides a powerful and flexible way to work with CSV files. You can use the read_csv() function to read a CSV file into a pandas DataFrame, and the to_csv() function to write a DataFrame to a CSV file.
import csv
import csv
data=[['name','age','salary'],
        ['sai',22,33000],
        ['kumar',20,24000],
        ['tej',32,34000]]
with open('emp.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(data)
with open('emp.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
        
'''
# import csv
# import os
# def write_emp_data():
#     data=[[31,'sai',22,33000],
#         [32,'kumar',20,24000],
#         [33,'tej',32,34000]]
#     with open('Emp.csv','w',newline='') as f:
#         writer=csv.writer(f)
#         writer.writerow(['id','name','age','salary'])
#         writer.writerows(data)
# def read_emp_data():
#     with open('Emp.csv','r') as f:
#         reader=csv.reader(f)
#         for row in reader:
#             print(row)
# def search_emp_data(emp_id):
#     with open('Emp.csv','r') as f:
#         reader=csv.reader(f)
#         for row in reader:
#             if row[0]==str(emp_id):
#                 print(row)
#                 break
#         else:
#             print('Employee not found')
# def delete_emp_data(emp_id):
#     lines=[]
#     with open('Emp.csv','r') as f:
#         reader=csv.reader(f)
#         for row in reader:
#             lines.append(row)
#             if row[0]==str(emp_id):
#                 lines.remove(row)
#     with open('Emp.csv','w',newline='') as f:
#         writer=csv.writer(f)
#         writer.writerows(lines)

# print(os.getcwd())
# print(os.chdir('C:\\Users\\G SAIKUMAR\\Desktop\\assignments'))
# write_emp_data()
# read_emp_data()
# search_emp_data(32)
# delete_emp_data(32)

import csv
import os


f=open('p.csv','r')
r=csv.reader(f)
for i in r:
    print(i)
f.close()
# data=[['id', 'name', 'age', 'salary'],
#       [31, 'sai', 22, 33000],
#       [32, 'kumar', 20, 24000],
#       [33, 'tej', 32, 34000]]
# with open('emp.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)
print(os.getcwd())
print(os.chdir('C:\\Users\\G SAIKUMAR\\Desktop\\assignments'))
with open('employee.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# l1=[(1,'sai',22,33000),
#     (2,'kumar',20,24000),
#     (3,'tej',32,34000)]
# with open('employee.csv','w',newline='') as f:
#     writer=csv.writer(f)
#     writer.writerow(['id','name','age','salary'])
#     writer.writerows(l1)
# with open('employee.csv','r') as f:
#     reader=csv.reader(f)
#     for row in reader:
#         print(row)