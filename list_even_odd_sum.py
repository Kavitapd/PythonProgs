#Programe to create a list with n values and calculate sum of even numbers and
#sum of odd numbers in the list
list1 =[]
n = int(input("enter number of values: "))
sum_e=0
sum_o=0
for i in list(range(n)):
    i=int(input("enter value: "))
    list1.append(i)
    if (i%2==0):
        sum_e+= i
    else:
        sum_o+= i
print("list is: ",list1)
print("sum of even numbers in list is: ",sum_e)
print("sum of odd numbers in list is: ",sum_o)
        
