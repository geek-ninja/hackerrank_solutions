# Electronic shop problem

b,n,m=map(int,input().split())
keyboard=list(map(int,input().split()))
drivers=list(map(int,input().split()))
result=[]
keyboard.sort()
drivers.sort()
for i in keyboard:
    for j in drivers:
        if i+j<=b:
            result.append(i+j)
if len(result)==0:
    print(-1)
else:
    print(max(result))
