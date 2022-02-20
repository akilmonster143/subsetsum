def tum(arr):
    Sum=0
    for k in range(0,len(arr)):
        Sum += (arr[k] * (k+1) * (len(arr)-k))
    return Sum
    
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    q=int(input())
    for j in range(q):
        q1=int(input())
        if(q1==1):
            arr.append(int(input()))
        if(q1==2):
            print(tum(arr))
