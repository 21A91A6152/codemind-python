n=int(input())
a=list(map(int,input().split()))
a=a[::-1]
j=0
d=0
for i in a:
    d=d+i*pow(2,j)
    j+=1
print(d)