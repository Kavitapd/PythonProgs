#program to count vowel in file1.txt
import sys
def main():
    try:
        f=open("file1.txt","r")
        vowelCount=0
        while True:
            ch=f.read(1)
            if ch=='':
                break
            elif ch in "aeiouAEIOU":
                vowelCount+=1
    except OSError:
        e=sys.exc_info()
        print(e)
    finally:
        f.close()
    print(f'total vowel in file1 is:{vowelCount}')
main()