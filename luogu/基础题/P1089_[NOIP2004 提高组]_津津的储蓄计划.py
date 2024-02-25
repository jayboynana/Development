# 成功ac

cost = []
for _ in range(12):
    cost.append(int(input()))
x = 0
c = 0
for i in range(len(cost)):
    x += 300-cost[i]
    if x > 100:
        c += (x-(x%100)) // 100
        x = x%100
    elif x < 0:
        print(-(i+1))
        break
    else:
        continue
if x >=0:
    print(x+c*120)