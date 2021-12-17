s=int(input())
a=[str(x) for x in input().split()]
m=[]
k={}
fon=0
for i in a:
    m.append("".join(sorted(i)))
for i in m:
    if i in k:
        k[i]+=1
    else:
        k[i]=1
max=0
for j in k:
    if k[j]>max:
        max=k[j]
print(max)

   
