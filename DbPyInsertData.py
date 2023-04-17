#WAP to insert marks in Student table
import mysql.connector
def main():
    cn=mysql.connector.connect(database='pythondb', username='root', password='Root321%')
    print("connection established")
    c=cn.cursor()
    #c.execute('''create table student(rollno int,name varchar(15),
              #sub1 int,sub2 int, total int,
              #avg float(10,2),result varchar(10))''')
    while True:
        rno=int(input("enter rollno: "))
        name=input("enter name: ")
        m1=int(input("enter marks1: "))
        m2=int(input("enter marks2: "))
         
        cmd= '''insert into student(rollno,name,sub1,sub2)
        values(%s,%s,%s,%s)''' 
        c.execute(cmd,params=(rno,name,m1,m2))
        a=c.rowcount
        if a==0:
            print("student details added")
        ans=input("add more student? ")
        if ans=='no':
            break
        
    cn.commit()
    cn.close()
    
main()    
        
