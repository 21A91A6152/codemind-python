s=input()
b=[]
sum=0
for i in s:
    if(i.isdigit()):
        b.append(int(i))
for j in b:
    sum=sum+j
print(sum)