n=input()
n=n.lower()
a=b=c=d=0
for i in n:
    if(i.isdigit()):
        c+=1
    if(i==" "):
        d+=1
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        a+=1
    else:
        b+=1
b=b-(d+c)
print("Vowels:",a,end='')
print()
print("Consonants:",b,end='')
print()
print("Digits:",c,end='')
print()
print("White spaces:",d,end='')
print()