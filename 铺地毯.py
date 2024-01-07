def find_top_carpet(n, carpets, x, y):
    top_carpet = -1

    for i in range(n-1, -1, -1):
        a, b, g, k = carpets[i]
        if a <= x <= a+g and b <= y <= b+k:
            top_carpet = i + 1
            break

    return top_carpet

# 读取输入
n = int(input())
carpets = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
print(carpets)
# 查找最上面的地毯
result = find_top_carpet(n, carpets, x, y)

# 输出结果
# print(result)



