l=input().split(',')
le=0
sub=""
for i in range(0,len(l[0])-1):
    for j in range(i+1,len(l[0])):
        if l[0][i:j] in l[1]:
            if len(l[0][i:j])>le:
                sub=l[0][i:j]
                le=len(sub)
                
print(sub)
                
