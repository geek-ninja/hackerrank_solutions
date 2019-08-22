p,d,m,s=map(int,input().split())
total=s;
count=0
if total-p>=m:
    total=total-p
    count+=1
    for i in range(p-d,m,-d):
        total-=i
        if total>=m:
            count+=1
while total>=m:
    total-=m
    count+=1
print(count)  
    
