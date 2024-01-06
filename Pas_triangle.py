import numpy as np
n=int(input())
arr=np.ones((n,n))
for i in range(2,n):
    for j in range(1,i):
        arr[i][j]=arr[i-1][j-1]+arr[i-1][j]

for i in range(n):
    j=i+1
    x=0
    while x<j:
        print(int(arr[i][x]),end=" ")
        x+=1
    print()