
def twosort(arr):
    arr.sort(key=lambda x:int(x),reverse= True)
    arr.sort(reverse=True,key=lambda x:x.count("2"))
    for i in arr:
        print(int(i),end=" ")
s=int(input())
arr=[(x) for x in input().split()]
twosort(arr)

