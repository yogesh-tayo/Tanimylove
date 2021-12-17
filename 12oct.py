
# a="Hello World"
# k=0
# m=a.strip()
# for i in range(len(m)):
#     if m[i]==" ":
#         k=0
#     else:
#         k+=1
# print(k)
# a=input().split()
# m=a
# print(len(m[-1]))
# a=input()
# m={}
# for i in a:
#     if i in m:
#         m[i]+=1
#     else:
#         m[i]=1
# # print(m)
# found=0
# for keys in m:
#     if m[keys]>0:
#         k=m.values()
#         found=1
# if found==1:
#     print(max(k))
# else:
#     print(0)

# a="academyiu"
# count=0
# for i in a:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         count+=1
# print(count)
# 0 1 2 3 5 8
# a=0
# b=1
# n=7
# for i in range(n):
#     print(a)
#     temp=a+b
#     a=b
#     b=temp
# n=5
# tri=[0]*n
# tri[0]=tri[1]=0
# tri[2]=1
# for i in range(3,n):
#     tri[i]=tri[i-1]+tri[i-2]+tri[i-3]
# print(tri[i])
a=[]
# c=2
# r=3
# mat = [[int(x) for x in input().split()] for y in range(r)]
# print(mat)
f=0
# if len(a)==1:
#     print(1)
#     continue
# if a[0]>a[1]:
#     print(1)
#     continue
# for i in range(1,len(a)):
#     if a[i]>a[i-1] and a[i]>a[i+1]:
#         print(i+1)
#         f=1
#         break
# if f==0:
#     if a[len(a)-1]>a[len(a)-2]:
#         print(len(a))
# else:
#     print(-1)
# order_num=int(input())         #O(1) ,#O(1)
# table_num=int(input())         #O(1) ,#O(1)
# res=[0]*table_num 
# print(res)             # O(1) ,#O(N)
# tablenumber=[]                 #O(1) ,#O(N)
# for i in range(order_num):     #O(1) ,#O(0)
#     tablenumber.append(int(input()))
#     print(tablenumber) #O(N) ,#O(1)
# for i in range(order_num):           #O(N) ,#O(1)
#     c=int(input())                   #O(1) ,#O(1)
#     index=tablenumber[i]  
#     print(index)           #O(N) ,#O(1)
#     res[index-1]+=c  
#     print(res)                #O(N) ,#O(0)
# max_cost=max(res)                    #O(1) ,#O(1)
# for i in range(len(res)):            #O(N) ,#O(0)
#     if res[i]==max_cost:             # O(N) ,#O(0)
#         print(i+1)                   # O(1) ,#O(0)
# TIME COMPLEXITY IS O(N)
# SPACE COMPLEXITY IS O(N)
# 
# k="my name is john."
# # m=k.replace(" ","spacex")
# # print(m)
# m=""
# for i in range(len(k)):
#     if k[i]==" ":
#         m+="spacex"
#     else:
#         m+=k[i]
# print(m)
# m="hello0ooooooo world"
# k=[]
# for i in m.split():
#     k.append(len(i))
# print(max(k))
# k=[1,2,3,4,5,6,7]
# m=3
# sum=0
# for i in k:
#     if i%m==0:
#         sum+=i
# print(sum)
# k=[2,5,4,10,1,3,7,8,11,13,6]
# m=[]
# n=[]
# for i in k:
#     if i%2==0:
#         m.append(i)
#     else:
#         n.append(i)
# # print(m)
# print(n+m)
# 
m=[]
k=['adf', 'qwert', 'a', 'rewq']
for i in k:
    print(i[1:])
        


    






   
    