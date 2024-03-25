# 回溯法超时
# dfs+剪枝 或者 动态规划

# def cc():
#     n, k = map(int, input().split())
#     result = []
#     def tracking(l):
#         if len(l) == k:
#             if set(l[:]) not in result and sum(l[:]) == n:
#                 result.append(set(l[:]))
#                 return
#             else:
#                 return
#         for i in range(1,n-k+2):
#             l.append(i)
#             tracking(l)
#             l.pop()
#     tracking([])
#     print(len(result))
#
# cc()

n, k = map(int, input().split())
cnt = 0
def dfs(last, sum, cur):
    global cnt
    if cur == k:
        if sum == n:
            cnt += 1
        return
    for i in range(last, n - sum + 1 ):# 进行剪枝操作
        if sum + i * (k - cur) > n:
            break
        dfs(i, sum + i, cur + 1)
    return cnt

c = dfs(1,0,0)
print(c)