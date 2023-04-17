n=int(input())
d1={}
marks=[]
if 2<=n<=10:
    for i in range(n):
        records=list(input().split())
        
        #print(records)
        key=records[0]
        val=records[1:]
        m_list=list(map(int,val))
        if len(m_list)!=3:
            
        d1[key]=m_list
        #print(key)
name=input()
marks=d1.get(name)
if marks:
    
   
       
        