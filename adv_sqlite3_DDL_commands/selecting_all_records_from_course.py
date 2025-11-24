import sqlite3

# insert
con=sqlite3.connect('student.db')

cur=con.cursor()

# d=cur.execute('select * from course').fetchone()
# print(d)  it will get only my first record in tuple formate

data=cur.execute('select * from course').fetchall() #it will get all records from my table 
print(data)  #it will show list of tuple data
con.commit()

cur.close()
con.close()