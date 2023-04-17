d1={'a':[2,3,4,1], 's':[2,4,7,8],'r':[1,3,6,8,9]}
l1=[]
for val in d1.values():
    l1=l1+val
print("list of all values in dict: ",l1)    
s=set(l1)
print("Set of values in dict: ",s)
l1=list(s)
l1.sort()
print("sorted unique val in dict: ",l1)

