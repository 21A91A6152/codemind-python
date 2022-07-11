n=input()
a=input()
for i in n:
    if(i==a):
        print(n.count(i))
        break
else:
    print("-1")