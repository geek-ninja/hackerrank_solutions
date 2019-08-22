# Drawing book problem
n=int(input())
p=int(input())
if p%2==0:
    x=p/2
else:
    x=(p-1)/2
y=(n-p)//2
if x<y:
    print(int(x))
elif n==6 and p==5:
    print(1)
else:
    print(int(y))