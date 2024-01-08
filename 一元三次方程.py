#暴力破解，只对一半
a,b,c,d=map(int,input().split())
l = []
for x in range(-100, 101,0.01):
    res = (a * x ** 3) + (b * x ** 2) + (c * x) + d
    if res == 0:
        l.append(x)
l = sorted(l)
l=["{:.2f}".format(i) for i in l]

print(*l)


