# 未ac

n = int(input())
row = 1
count = 0
m = True
# 从第一行开始，依次枚举每一行的有理数
while m:
    for i in range(1, row + 1):
        count += 1
        if count == n:
            if row % 2 == 1:
                print(f"{row - i + 1}/{i}")
                m = False
                break
            else:
                print(f"{i}/{row - i + 1}")
                m = False
                break
    row += 1