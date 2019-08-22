n=int(input())
arr=[]
for _ in range(n):
    arr.append(input())
for i in sorted(sorted(arr), key=len):
	print(i)