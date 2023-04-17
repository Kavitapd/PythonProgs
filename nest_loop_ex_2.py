#display prime num from given list
l1=[7,34,56,34,11,68,24]
#rem
for i in l1:
    s=0
    for n in range(1,i+1):
        #rem=i%n
        if i%n==0:
            s+=1
    if s>2:        
        print(i," prime")
    else:
        print(i," not prime")    