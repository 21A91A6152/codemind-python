n=input()
n=n.lower()
m=input()
m=m.lower()
if(len(m)==len(n)):
    for i in n:
        if i not in m:
            print(False)
            break
    else:
        print(True)
else:
    print(False)
 