# def unitdistance(temp1, temp2):
#     m = len(temp1)
#     n = len(temp2)
#     if abs(m - n) > 1:
#         return False
#     count = 0   
#     i = 0
#     j = 0
#     while i < m and j < n:
#         if temp1[i] != temp2[j]:
#             if count == 1:
#                 return False
#             if m > n:
#                 i+=1
#             elif m < n:
#                 j+=1
#             else:    
#                 i+=1
#                 j+=1
#             count+=1
#         else:    
#             i+=1
#             j+=1
#     if i < m or j < n:
#         count+=1
#     return count == 1
# for i in range(int(input())):
#     m,n=input().split()
#     print(unitdistance(m,n))
# your code goes here
# def singlenum(k):
# 	m={}
# 	for i in k:
# 		if i in m:
# 			m[i]+=1
# 		else:
# 			m[i]=1
# 	for keys in m:
# 		if m[keys]==1:
# 			print(keys)
# k=[]
# for i in range(int(input())):
# 	k.append(int(input()))
# singlenum(k)

# def tt(k,tag):
#     i=0
#     j=len(k)-1
#     while i<j:
#         if k[i]+k[j]==tag:
#             return True
#         elif k[i]+k[j]<tag:
#             i+=1
#         else:
#             j-=1
#     return False
# k=[1 ,-5 ,6, 12, 9]
# k.sort()
# target=11
# print(tt(k,target))
# m,n=map(int,input().split())
# found=0
# s=set()
# arr=[int(x) for x in input().split()]
# for i in range(0,len(arr)):
#     found+=arr[i]
#     print(found)
#     if found==n or found in s:
#         print(True)
#     s.add(found)
# print(False)
n,x=map(int,input().split())
num=list(map(int,input().split()[:n]))
flag=0
for j in range(n):
    SUM=0
    for i in range(len(num)):
         SUM+=num[i]
    if SUM-num[j]==x:
        flag=1
        break
    else:
        continue
print(flag)
	

