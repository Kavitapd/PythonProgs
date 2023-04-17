#WAP to update total, ag,result of student marks of student table
import mysql.connector as mysql
def main():
    cn=mysql.connect(database='pythondb',username='root',password='Root321%')
    c=cn.cursor()
    cmd1= "update student set total=sub1+sub2"
    cmd2='update student set avg=total/2'
    cmd3='update student set result="Pass" where sub1>=40 and sub2>=40'
    cmd4='update student set result="Fail" where sub1<40 and sub2<40'
    c.execute(cmd1)
    c.execute(cmd2)
    c.execute(cmd3)
    c.execute(cmd4)
    print('student details updated.')
    cn.commit()
    cn.close()
main()    