import sqlite3

co=sqlite3.connect('student.db')
cor=co.cursor()

for i in range(5):
    id=input('ENter id')
    Person_name=input('Enter your name')
    Course_name=input('enter course name')
    cor.execute(f'insert into course values({id},"{Person_name}","{Course_name}")')
    co.commit()

cor.close()
co.close()
