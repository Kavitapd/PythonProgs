# program to write odd number in any range.
start=int(input("enter start value: "))
stop=int(input ("enter stop value: "))
print("Odd numbers between given range are: ")
for n in range(start,stop+1):
    if(n%2!= 0):
        print(n)
