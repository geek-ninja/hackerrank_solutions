s=input()
t=input()
n=int(input())
if s==t:
    x=2*len(s)
    if n>=x:
        print("Yes")
    else:
        print("No")
elif len(s)>len(t):
    x=0
    for i in range(len(t)):
        if s[i]!=t[i]:
            x+=1
    x=(2*x)+len(s)-len(t)
    if n>=x:
        print("Yes")
    else:
        print("No")
else:
    x=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            x+=1
    x=(2*x)+len(t)-len(s)
    if n>=x:
        print("Yes")
    else:
        print("No")