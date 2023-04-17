#program to insert n values in a list
n=int(input("Enter length of list: "))
list1=[]
print("enter",n,"elements of list: ")
for i in range(n):
    list1.append(int(input()))
print("The list is:",list1)
