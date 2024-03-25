# 已ac

a1,a2,n = map(int,input().split())

an = a1+(a2-a1)*(n-1)
print(int((a1+an)*n//2))