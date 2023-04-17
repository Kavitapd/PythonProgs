#write a programe to swap any two elements in a list .
list1 = [10,20,30,40,50]
print("Length of list is: ",len(list1))
pos1 = int(input("enter 1st position: "))
pos2 = int(input("enter 2nd position: "))
list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
print(list1)
                                          
