def alternate(arr):
	odd=[]
	even=[]
	for i in range(len(arr)):
		if i%2==0:
			even.append(arr[i])
		else:
			odd.append(arr[i])
	even.sort(reverse=True)
	odd.sort()
	for i in range(len(even)):
		arr[2*i]=even[i]
	for i in range(len(odd)):
		arr[2*i+1]=odd[i]
	return arr
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        arr=[int(x) for x in input().split()]
        print(*alternate(arr))