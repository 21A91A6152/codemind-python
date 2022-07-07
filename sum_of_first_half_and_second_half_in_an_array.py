n=int(input())
a=list(map(int,input().split()))
sf=0
se=0
if(n%2==0):
    for i in range(n//2):
        sf+=a[i]
    for j in range((n//2),n):
        se+=a[j]
    print(sf)
    print(se)
else:
    for i in range(n//2):
        sf+=a[i]
    for j in range((n//2),n):
        se+=a[j]
    print(sf)
    print(se)