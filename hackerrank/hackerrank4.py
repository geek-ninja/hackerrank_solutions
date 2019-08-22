from itertools import combinations_with_replacement
y=[]
s=raw_input().split()
k=int(s[1])
x=(list(combinations_with_replacement(s[0],k)))
for i in x:
    y.append(''.join(i))
y.sort()
print(y)
