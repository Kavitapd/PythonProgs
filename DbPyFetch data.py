import mysql.connector
def main():
    cn=mysql.connector.connect(database='pythondb',username='root',password='Root321%')
    c=cn.cursor()
    c.execute('select * from student')
    row=c.fetchone()
    print("one row",row)
    rows=c.fetchmany(2)
    print("2 rows",rows)
    all_rows=c.fetchall()
    print("all rows",all_rows)
main()