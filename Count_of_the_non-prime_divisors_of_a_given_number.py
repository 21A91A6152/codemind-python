def prime(a):
    for j in range(2,int(a**0.5)+1):
        if a%j==0:
            return 0
    return 1
n=int(input())
c=0
for i in range(2,n+1):
    if(n%i==0 and prime(i))==1:
        c+=1
d=0
for i in range(1,n+1):
    if(n%i==0):
        d=d+1
print(d-c)
        