# val=int(input())
# count=0
# arr = map(int,input().split())
# for i in (arr):  
#     if i%2==0:
#         count+=i
# print(count)
n=int(input())
sum=0
arr=list(map(int,input().split()))
for i in range(n):
    if(arr[i]%2==0):
       sum=sum+arr[i]
print(sum)