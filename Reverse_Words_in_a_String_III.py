n=input()
x=list(n.split(" "))
y=[]
for i in x:
  y.append(i[::-1])  
print(*y)