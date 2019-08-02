n=list(map(int,input().split(" ")))
def binaryfun(i):
    s=""
    while(i>0):
        s+=str(i%2)
        i=i//2
    return s[::-1]

binary=[]
for i in n:
    binary.append(binaryfun(i))
for i in binary:
    if "00" in i or "11" in i:
        print(0)
    else:
        print(1)
    
