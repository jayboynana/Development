# dict_data = {'1000': 90, '3239': 88, '2390': 95, '7231':84 , '1005': 95, '1001': 88}
# l = sorted(dict_data.items(), key=lambda item: [-item[1], item[0]])
# print(l)

def getLayer(data, n, x, y):
    carpet = -1
    for i in range(n - 1, -1, -1):
        a, b, g, k = data[i]
        if a <= x <= a + g and b <= y <= b + k:
            carpet = i + 1
            return carpet
    return carpet


n = int(input())
input_data = [list(map(int, input().split(" "))) for _ in range(n)]
x, y = map(int, input().split(" "))
print(getLayer(input_data, n, x, y))
