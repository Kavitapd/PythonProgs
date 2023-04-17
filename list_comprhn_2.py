l1=[10,3,4,37,8]
l2=[]
for i in l1:
    if i%2==0:
        l2.append(i)
print(l2)    
l3=[val for val in l1 if val%2!=0]
print(l3)