#Program to write even number in a range
n =int(input("enter the range: "))
print("the even numbers between 0 to",n,"are: ")
for i in range(n+1):
    if(i%2==0):
         print(i)
