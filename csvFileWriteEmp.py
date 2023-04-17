import csv 
import sys
def main():
    try:
        f=open("emp.csv","w",newline='')
        csvwr=csv.writer(f)
        csvwr.writerow(['empno','ename','salary'])
        while True:
            empno=int(input("enter EmployeeNo:"))
            ename=input("enter emp name: ")
            salary=eval(input("enter salary: "))
            csvwr.writerow([empno,ename,salary])
            ans=input("add another emp? ")
            if ans=='no':
                break
    except:
        t=sys.exc_info()
        print(t[1])
    finally:
        f.close()
        
main()
            
            