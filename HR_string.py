s=input()
l=list(s)
i,ch=input().split()
if int(i)<= len(l):
    l[int(i)]=ch
string=''.join(l)    
print(string)    
