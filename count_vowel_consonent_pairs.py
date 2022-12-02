n=input()
m=n[::-1]
c=0
for i in range(int(len(n)/2)):
    if(n[i] in "aeiouAEIOU"):
        if(m[i] not in "aeiouAEIOU "):
            c+=1
    if(n[i] not in "aeiouAEIOU  "):
        if(m[i] in "aeiouAEIOU"):
            c+=1
             
print(c)