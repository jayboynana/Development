# 未ac,ac一部分

from decimal import Decimal, ROUND_HALF_UP

correct = []
r = []
while True:
    current = input()
    if current == 'EOF':
        break
    else:
        correct.append(current)
while True:
    r_current = input()
    if r_current == 'EOF':
        break
    else:
        r.append(r_current)
t = int(input())

c = 0
for i, r_str in enumerate(r):
    while r_str.find('<') != -1:
        if r_str.find('<') == 0:
            l_str = list(r_str)
            l_str.pop(0)
            r_str = ''.join(l_str)
        else:
            r_str = r_str.replace(r_str[r_str.find('<')-1]+'<','')
    if r_str.find('<') == -1:
        for j in range(min(len(correct[i]),len(r_str))):
            if r_str[j] == correct[i][j]:
                c += 1
t = t / 60
print(Decimal(c/t).quantize(Decimal(1.),rounding=ROUND_HALF_UP))