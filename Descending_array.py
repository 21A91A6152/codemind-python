n=int(input())
arr=list(map(int,input().split()))
b=[]
c=0
for i in arr:
    b.append(i)
temp = 0;    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] < arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
for i in range(0, len(arr)):     
    if(b[i]==arr[i]):
        c+=1
if(c==n):
    print("yes")
else:
    print("no")
    