l=list(map(int,input().split(" ")))
n=l[0]
l=l[1:]
if n==1:
    print(l[0])
elif n==2:
    print(l[1])
elif n==3:
    print(l[2])
else:   
    for i in range(4,n+1):
        s=sum(l[-3:])
        l.append(s)
    print(l[-1])
    
