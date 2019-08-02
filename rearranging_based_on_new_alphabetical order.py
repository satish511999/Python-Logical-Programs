#alpha=input().split(" ")
alpha=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
val=[]
strs=[]
inp=int(input())
for i in range(0,inp):
    strs.append(input())
'''
for i in strs:
    count=1
    for j in i:
        count*=alpha.index(j.upper())
    val.append(count)
'''
lens=[]
for i in strs:
    lens.append(len(i))
maxlen=max(lens)
for i in strs:
    count=""
    for j in i:
        if (alpha.index(j.upper())+1)<=9:
            count+='0'
        count+=str(alpha.index(j.upper())+1)    
    if len(i)<maxlen:
        diff=(maxlen-len(i))*2
        count+='0'*diff
    val.append(int(count))

zi=sorted(zip(val,strs))
for i in zi:
    print(i[1])
        
    
