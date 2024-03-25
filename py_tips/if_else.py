# 注意if的使用方法
def panduan(a,b,c):
    # 只能走其中一个
    if a == 0:
        print(a)
    elif b == 1:
        print(b)
    else:
        print(c)

def panduan1(a,b,c):
    # 三个if独立，可以进入三个if
    if a == 0:
        print(a)
    if b == 1:
        print(b)
    if c == 2:
        print(c)

panduan(0,1,3)
print(' ')
panduan1(0,1,3)