import sys
def main():
    try:
        f=open("marks.txt","w")
        while True:
            rollno=int(input("enter roll num: "))
            sub1= int(input("enter sub1 marks: "))
            sub2= int(input("enter sub2 marks: "))
            print(rollno,sub1,sub2,file=f)
            ans= input("add another student?")
            if ans =="no":
                break
    except OSError:
        e=sys.exc_info()
        print(e[1])
    finally:
        f.close()
main()