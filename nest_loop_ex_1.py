#prog to find factorial of given num
n=int(input("enter num: "))
fact=1
for i in range(1,n+1):
    fact*=i
    print(fact)