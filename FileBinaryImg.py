#prog to copy content of one imag to another
import sys
def main():
    try:
        f1=open("Screenshot 2023-03-12 114431.png","rb")
        f2=open("pic1.png","wb")
        b=f1.read()
        f2.write(b)
        print (type(b))
    except :
       t=sys.exc_info()    
       print(t[1])
    finally:
        f1.close()
        f2.close()
main()
        