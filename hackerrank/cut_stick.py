n=int(input())
arr=[]
c=0
arr=list(map(int,input().split()))
arr.sort()
check=arr.copy()
check=list(set(check))
check.sort()
print(n)
for i in check:
    c+=arr.count(i)
    if (n-c)!=0:
        print(n-c)
    