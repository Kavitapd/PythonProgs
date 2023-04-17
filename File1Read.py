#program to read content of file1.txt
import sys
def main():
    try:
        file=open("file1.txt","r")
        strVal=file.read()
        print(strVal)
    except OSError:
        e=sys.exc_info()
        print(e)
    finally:
        file.close()
main()
