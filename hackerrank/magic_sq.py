# magic square problem 
def row_sum_check(array):
    if sum(array[0])==sum(array[1]) and sum(array[1])==sum(array[2]):
        return 1
    else:
        return 0
def column_sum_check(array):
    c1=(array[0][0]+array[1][0]+array[2][0])
    c2=(array[0][1]+array[1][1]+array[2][1])
    c3=(array[0][2]+array[1][2]+array[2][2])        
    if c1==c2 and c2==c3:
        return 1
    else:
        return 0
def dig_sum_check(array):
    d1=array[0][0]+array[1][1]+array[2][2]
    d2=array[0][2]+array[1][1]+array[2][0]
    if d1==d2:
        return 1
    else:
        return 0
array=[]
p=list(map(int,input().split()))
array.append(p)
q=list(map(int,input().split()))
array.append(q)
r=list(map(int,input().split()))
array.append(r)
x=row_sum_check(array)
y=column_sum_check(array)
z=dig_sum_check(array)
