marks=[]
students=[]
for _ in range(int(input())):
    name=raw_input()
    mark=float(input())
    students.append([name,mark])
    marks.append(mark)
x=sorted(marks)[1]
for a,b in students:
    if b==x:
        print(a)