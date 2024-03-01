# 成功ac

ah = list(map(int,input().split()))
tth = int(input())
c = 0
for h in ah:
    if h <= tth+30:
        c += 1
print(c)