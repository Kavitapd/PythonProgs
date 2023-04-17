#Program to read and calculate total marks and 
#find average and result
def main():
    try:
        f=open("marks.txt","r")
        while True:
            record=f.readline() 
            
            if record!='':
                rollno,sub1,sub2= [int(rec) for rec in record.split()] #map(int,record.split())
                total=sub1+sub2
                avg=total/2
                print(f'Total Marks= {total}')
                print(f'avg= {avg}')
                if sub1>40 and sub2>40:
                    print('pass')
                else:
                    print("Fail") 
            else:
                break
    except OSError:
        print("reading error")   
        
main()
                  