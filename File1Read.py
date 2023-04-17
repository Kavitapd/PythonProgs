#program to read content of file1.txt
import sys
def main():
    try:
        f=open("file1.txt","r")
        s=f.read()
        print(s)
    except OSError:
        e=sys.exc_info()
        print(e)
    finally:
        f.close()
main()