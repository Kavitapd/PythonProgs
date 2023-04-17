import csv
import sys
def main():
    try:
        f=open("Student.csv","w",newline='')
        dw=csv.DictWriter(f,fieldnames=['rollno','name','course'])
        dw.writeheader()
        while True:
            rno=int(input("rollno: "))
            name=input("name: ")
            course=input("course: ")
            row={'rollno':rno,'name':name,'course':course}
            dw.writerow(row)
            ans=input("add another emp? ")
            if ans=='no':
                break
    except:
        t=sys.exc_info()
        print(t[1])
    finally:
        f.close()
        
main()    