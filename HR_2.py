n= int(input())
if 2<=n<=10:
    A=list(map(int,input().split()))
    if -100<=A[i]<=100:
        A.sort(reverse=True)
        c=A.count(max(A))
        print(A[c])    
        