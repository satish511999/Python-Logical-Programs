dire=['r','d','l','u']
ini=[1,1,2,2]
n=int(input())
m=int(n**0.5)+1
count=1
spiral=[]
for i in range(0,m):
    row=[]
    for j in range(0,m):
        row.append('*')
    spiral.append(row)
di='r'
r=0
c=0
if m%2==0:
    r=m/2-1
    c=m/2-1
else:
    r=m//2
    c=m//2
r=int(r)
c=int(c)
spiral[r][c]=count
count+=1
c+=1
while(count<=n):
    val=ini[dire.index(di)]
    while(val!=0):
        spiral[r][c]=count
        count+=1
        if count>n:
            break
        val-=1
        if val>0:
            if di=='d':
                r+=1
            elif di=='r':
                c+=1
            elif di=='l':
                c-=1
            elif di=='u':
                r-=1
    
    ini[dire.index(di)]+=2
    
    if di=='u':
        di='r'
    else:
        di=dire[dire.index(di)+1]
    if di=='d':
        r+=1
    elif di=='r':
        c+=1
    elif di=='l':
        c-=1
    elif di=='u':
        r-=1
for i in spiral:
    for j in i:
        if j!="*":
            j=str(j)
            if len(str(j))==1:
                j=' '+str(j)
            print(str(j)+" ",end=" ")
        else:
            print("   ",end=" ")
    print()
    
