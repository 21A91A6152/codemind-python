n=input()
x=list(n.split(" "))
a=[]
for i in range(len(x)):
    a.append(min(x[i]))
    a.append(max(x[i]))
print(*a)