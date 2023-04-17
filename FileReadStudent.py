#Program to read content of Student.txt file

def main():
    try:
        f=open("student.txt","r")
        while True:
            record=f.readline()
            if record!='':
                rollno,name,course=record.split(",")
                print(f'{rollno},{name},{course}')
            else:
                break
    except OSError:
        print("reading error")
    finally:
        f.close()
    
    
main()