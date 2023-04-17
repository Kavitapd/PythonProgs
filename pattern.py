for  r in range(1,6):
    for c in range(1,r+1):
        print(r,end='')
    print() 
print()       
for r in range(5,0,-1):
    for c in range(1,r+1):
        print(r,end='')    
    print()    
print()
for r in range(1,6):
    for c in range(1,r+1):
        print(c,end='')
    print()    
print()
for r in range(5,0,-1):
    for c in range(1,r+1):
        print(c,end='')
    print()    
print()
for r in range(1,6):
    for c in range(1,6):
        print(r,end='')
    print()        
print()
for r in range(5,0,-1):
    for c in range(1,6):
        print(r,end='')
    print()         
print()
for r in range(1,6):
    for c in range(5,0,-1):
        if c<= r:
            print(c,end='')
        else:
            print(' ',end='')
    print()        
    