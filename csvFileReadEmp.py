import csv
import sys
def main():
    try:
        f=open("emp.csv","r",newline='')
        csvr=csv.reader(f)
        emplist=list(csvr)
        for i in range(1,len(emplist)):
            print(emplist[i][0],emplist[i][1],emplist[i][2])
    except:
        t=sys.exc_info()
        print(t[1])
    finally:
        f.close()
        
main()