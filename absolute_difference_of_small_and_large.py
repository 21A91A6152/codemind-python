n=input()
x=list(n.split(" "))
for i in range(len(x)):
    a=b=0
    a=ord(min(x[i]))
    b=ord(max(x[i]))
    print(abs(a-b),end=" ")