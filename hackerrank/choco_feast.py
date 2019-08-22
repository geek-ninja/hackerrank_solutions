t=int(input())
for _ in range(t):
    n,c,m=map(int,input().split())
    chocolate=n//c
    wrapper=chocolate//m+chocolate%m
    chocolate=chocolate+chocolate//m
    while wrapper>=m:
        chocolate=chocolate+wrapper//m
        wrapper=wrapper//m+wrapper%m
    print(chocolate)
