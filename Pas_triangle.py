# import numpy as np
# n=int(input())
# arr=np.ones((n,n))
# for i in range(2,n):
#     for j in range(1,i):
#         arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
#
# for i in range(n):
#     j=i+1
#     x=0
#     while x<j:
#         print(int(arr[i][x]),end=" ")
#         x+=1
#     print()
# l=[1,2,3,4,5,6,7]
# value=100
# try:
#     i=l.index(value)
#     print(i+1)
# except Exception as e:
#     print(e)

if __name__ == "__main__":
    l=[10,20,30,40,50]
    for k,v in enumerate(l,1):
        print(f"{k}:{v}")
