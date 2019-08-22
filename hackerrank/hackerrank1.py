n=int(input())
student={}
for i in range(n):
	line=raw_input().split()
	name=line[0]
	avg=(sum(list(map(float,line[1:4]))))/3
	student[name]=avg
find=raw_input()
print("%.2f"%(student[find]))



