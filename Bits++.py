n=int(input())
x=0
for k in range(n):
    a=input()
    for i in a:
        if(i=='+'):
            x+=1
            break
        if(i=="-"):
            x-=1
            break
print(x)
    