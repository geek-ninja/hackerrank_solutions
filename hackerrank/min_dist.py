n=int(input())
a=list(map(int,input().split()))
result=[]
c=0
for i in range(n):
    if a.count(a[i])>1:
        store=a[i]
        a[i]=0
        result.append(abs(i-a.index(store)))
if len(result)==0:
    print(-1)
else:
    print(min(result))

        