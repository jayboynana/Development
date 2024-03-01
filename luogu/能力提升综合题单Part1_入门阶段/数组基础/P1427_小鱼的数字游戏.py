# 成功ac

s = list(map(int, input().split()))
s = s[::-1]
for num in s:
    if num == 0:
        continue
    print(num,end=' ')