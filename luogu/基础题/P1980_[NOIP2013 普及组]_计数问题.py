# ac一部分，超时

n,x = map(int,input().split())
c = 0
for i in range(1,n+1):
    c += str(i).count(str(x))
print(c)

