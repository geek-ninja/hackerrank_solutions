original_string=input()
sub_string=input()
c=0
length_org=len( original_string)
length_sub=len(sub_string)
for i in range(length_org):
    if sub_string==(original_string[i:length_sub+i]):
        c+=1
print(c)