# Picking Numbers
n=int(input())
arr=list(map(int, input().split()))
result=[]
check_arr=list(set(arr))
check_arr.sort()


for i in range(len(check_arr)-1):
    if abs(check_arr[i]-check_arr[i+1])<=1:
        result.append(arr.count(check_arr[i])+arr.count(check_arr[i+1]))
print(max(result))


    