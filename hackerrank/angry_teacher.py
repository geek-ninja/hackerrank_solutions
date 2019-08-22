# Angry professor problem
t=int(input())
for _ in range(t):
    n,k=map(int, input().split())
    attendance=list(map(int,input().split()))
    present=filter(lambda x: True if x<=0 else False,attendance)
    if len(list(present))>=k:
        print("NO")
    else:
        print("YES")