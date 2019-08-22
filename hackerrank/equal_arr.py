n=int(input())
arr=list(map(int,input().split()))
check=[]
arr1=arr.copy()
arr1=list(set(arr1))
for i in arr1:
    check.append(arr.count(i))
print(n-(max(check)))