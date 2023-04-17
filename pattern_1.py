n=0
for r in range(1,6):
    for c in range(1,r+1):
        n+=1
        print(n,end='')
    print()    
print()    
for r in range(1,6):
    for c in range(1,r+1):
        if c%2==0:
           print("0",end='')
        else:
            print("1",end='')   
    print()  
print()
space =4
for r in range(1,6):
    for s in range(space):
        print(" ",end='')
    for c in range(1,r+1):    
        print("*",end='') 
    space=space-1      
    print()  

