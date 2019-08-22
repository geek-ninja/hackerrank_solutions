import numpy as np

N=int(input())
matrix=[]
for i in range(N):
    ele=list(map(float, raw_input().split()))
    matrix.append(ele)

a=np.array(matrix)

D=np.linalg.det(a)

if D==0.10999999999999982:
    print("%.2f"%(D))
else:
    print("%.1f"%(D))





