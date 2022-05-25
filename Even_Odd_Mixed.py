n=int(input())
c=0
d=0
while(n):
    i=n%10
    n=n//10
    if(i%2==0):
        c+=1
    else:
        d+=1
if(c>0 and d<1):
    print("Even")
elif(c<1 and d>0):
    print("Odd")
else:
    print("Mixed")