n=input()
n=n.lower()
arr=list(n.split(" "))
c=0
for i in arr:
    y=i[::-1]
    if(i==y):
        c+=1
print(c)