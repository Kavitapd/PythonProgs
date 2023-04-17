def main():
    try:
        f=open("student.txt","a")
        while True:
            rollno=int(input("enter roll num: "))
            name= input("enter name: ")
            course= input("enter course: ")
            record=f'{rollno},{name},{course}\n'
            f.write(record)
            ans= input("add another student?")
            if ans =="no":
                break
    except OSError:
        print("Error in creating file")
    finally:
        f.close()
main()
        
    