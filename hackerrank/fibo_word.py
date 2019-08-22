# Project Euler,Fibonacci Words problem
q=int(input())
for _ in range(q):
    a,b,n=input().split()
    n=int(n)
    next_seq=''
    final_seq=0
    for i in range(n):
        next_seq=a+b
        a=b
        b=next_seq
        final_seq=len(next_seq)
    print(next_seq[n-1])
        
    
    
    
    