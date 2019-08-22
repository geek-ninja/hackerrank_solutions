n,k,q=map(int,input().split())
arr=list(map(int,input().split()))
rotated_arr=[]
query=[0 for i in range(n)]
for i in range(n):
    x=arr[i]
    j=i
    if (j+k)>n-1:
        j=((j+k)%n)
        rotated_arr.insert(j,x)
    else:
        j=j+k
        rotated_arr.insert(j,x)
for j in range(q):
    print(rotated_arr[int(input())])
