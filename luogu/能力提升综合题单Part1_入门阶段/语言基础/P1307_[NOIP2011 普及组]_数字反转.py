# 成功ac

x = int(input())
if x == 0:
    print(x)
elif x < 0:
    print(-int(str(x)[1:][::-1]))
else:
    print(int(str(x)[::-1]))