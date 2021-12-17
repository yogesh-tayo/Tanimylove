# num=input()
# found=0
# ls=["a","e","i","o","u"]
# k=[]
# for i in num:
#     if i in ls and i not in k:
#         found=1
#         k.append(i)
# if found==1 and len(ls)==len(k):
#     print(1)
# else:
#     print(-1)
# Complete this addStrings() function

# Complete this addStrings() function

def addStrings(num1, num2):
    p1, p2 = len(num1)-1, len(num2)-1
    val = []
    carry = 0
    while p1 >= 0 or p2 >= 0 or carry:
        d1 = int(num1[p1]) 
        d2 = int(num2[p2])
        sum = d1+d2+carry
        carry, digit = sum//10, sum%10
        val.append(str(digit))
        p1 -= 1
        p2 -= 1
        
    return "".join(val[::-1])
    ## Do not change anything below this line:

for _ in range(int(input())):
    n1, n2 = input().split()
    print(addStrings(n1,n2))