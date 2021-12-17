n = int(input())
list1 = []
for i in range(0,n):
    list1.append(int(input()))
list1.sort()
if(list1[-1]+list1[-2] < 100):
    print('False')
else:
    print('True')