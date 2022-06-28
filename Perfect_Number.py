n=int(input())
temp=n
c=0
for i in range(1,n):
    if(n%i==0):
        c+=i
if(c==temp):
    print(True)
else:
    print(False)
    