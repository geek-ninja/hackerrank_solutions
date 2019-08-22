# migtory bird problem 
spoting=[]
n=int(input())
arr=list(map(int, input().split()))
species=list(set(arr))
species.sort()
for i in species:
    spoting.append(arr.count(i))

x=spoting.index((max(spoting)))
print(species[x])

