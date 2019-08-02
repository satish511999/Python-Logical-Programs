d={1:3,2:3,3:5,5:4,6:3,7:5,8:5,9:4,4:4,10:3,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:7,19:7}
n=int(input())
count=0
for i in range(1,n+1):
    if len(str(i))==1:
        count+=d[i]
    elif len(str(i))==2:
        if str(i)[-1]=='0':
            count+=d[i]
        elif str(i)[0]=='1':
            count+=d[i]
        else:
            p2=i%10
            p1=i-p2
            count+=d[p2]+d[p1]
    else:
        count+=7
print(count)
    
