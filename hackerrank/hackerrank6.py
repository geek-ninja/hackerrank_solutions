def hcf(array):
    array.sort()
    for i in range(1,array[0]+1):
        for j in array:
            if j%i==0:
                x=i
    return x

array=[]
check=[]
n,m=map(int, input().split())
array1=list(map(int, input().split()))
y=max(array1)
array2=list(map(int, input().split()))
x=hcf(array2)

e=0
for i in range(y,x+1):
    c=0
    for j in array1:
        if i%j==0:
            c+=1
            if c==n:
                check.append(i)

for i in check:
    d=0
    for j in array2:
        if j%i==0:
            d+=1
            if d==m:
                e+=1
print(e)
        
    