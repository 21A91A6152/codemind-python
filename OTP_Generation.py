n=int(input())
x=0
while(n):
    j=n%10
    x=x*10+j
    n=n//10
while(x):
    i=x%10
    x=x//10
    if(i%2==0):
        continue
    else:
        k=i*i
        print(k,end='')
        
        