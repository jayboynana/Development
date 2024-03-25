# 记忆化搜索
# 看题解，c++转python后ac

import numpy as np

l = []
mem = np.zeros((25,25,25))

while True:
    s = list(map(int,input().split()))
    if -1 in set(s) and len(set(s)) == 1:
        break
    l.append(s)

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(20,20,20)
    elif a < b < c:
        if mem[a][b][c-1] == 0:
            mem[a][b][c-1] = w(a,b,c-1)
        if mem[a][b-1][c-1] == 0:
            mem[a][b-1][c-1] = w(a,b-1,c-1)
        if mem[a][b-1][c] == 0:
            mem[a][b-1][c] = w(a,b-1,c)
        mem[a][b][c] = mem[a][b][c-1] + mem[a][b-1][c-1] - mem[a][b-1][c]
        # return w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        if mem[a-1][b][c] == 0:
            mem[a-1][b][c] = w(a-1,b,c)
        if mem[a-1][b-1][c] == 0:
            mem[a - 1][b - 1][c] = w(a-1,b-1,c)
        if mem[a-1][b][c-1] == 0:
            mem[a - 1][b][c - 1] = w(a-1,b,c-1)
        if mem[a-1][b-1][c-1] == 0:
            mem[a - 1][b-1][c - 1] = w(a-1,b-1,c-1)
        mem[a][b][c] = mem[a-1][b][c] + mem[a - 1][b - 1][c] + mem[a - 1][b][c - 1] - mem[a-1][b-1][c-1]
        # return w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return mem[a][b][c]

for sub in l:
    r = int(w(sub[0],sub[1],sub[2]))
    print(f'w({sub[0]}, {sub[1]}, {sub[2]}) = {r}')