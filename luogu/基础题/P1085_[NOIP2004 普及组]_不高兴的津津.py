# 成功ac

sche = {}
for i in range(1,8):
    sche[i] = list(map(int,input().split()))
d = 0
max_index = 0
for item in sche.items():
    today = sum(item[1]) - 8
    if today > d:
        d = today
        max_index = item[0]
print(max_index)