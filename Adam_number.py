n=int(input())
p=n*n
sumq=0
sumn=0
while(n):
    i=n%10
    sumn=sumn*10+i
    n=n//10
q=sumn*sumn
while(q):
    j=q%10
    sumq=sumq*10+j
    q=q//10
if(sumq==p):
    print(True)
else:
    print(False)