a=input()
b=input()
a=a.lower()
b=b.lower()
n=len(a)
for i in a:
    if i not in b:
        print(False)
        break
else:
    print(True)
        