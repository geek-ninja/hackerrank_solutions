# Beautiful day at movie

def reverse(string):
    rev_str="".join(reversed(string))
    return rev_str
i,j,k=map(int,input().split())
count=0
for a in range(i,j+1):
    result=abs(a-(int(reverse(str(a)))))
    if result%k==0:
        count+=1
print(count)