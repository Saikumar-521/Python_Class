import sqlite3

c=sqlite3.connect('student.db') #its already exits and we create another table coures table

cor=c.cursor()

cor.execute('create table course(id interger primary key,Person_name text,course_name text)')
c.commit()

cor.close()
c.close()

