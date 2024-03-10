# 成功ac

word = input().lower()
p = input().lower()
c = 0
index = None
for i,w in enumerate(p.split(' ')):
    if word == w and index is None:
        index = i
        c += 1
    elif word == w and index is not None:
        c += 1
if c == 0:
    print(-1)
else:
    l = 0
    for i,w in enumerate(p.split(' ')):
        if i != index:
            l += len(w)+1
        else:
            break
    print(c,l,sep=' ')
