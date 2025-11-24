import sqlite3

con=sqlite3.connect('student.db')

cur=con.cursor()
# cur.execute('alter table  student rename to students') 
# con.commit()

# d=cur.execute('select * from student').fetchone()  sqlite3.OperationalError: no such table: student


d=cur.execute('select * from students').fetchone()
print(d)
con.commit()
# now rename the existing colmun name name colmun to student_name

# cur.execute('alter table students rename column name to student_name')
# con.commit()

cur.execute('select * from students')
schema=cur.fetchone()

print('Table Schema: \n',schema)
cur.close()
con.close()