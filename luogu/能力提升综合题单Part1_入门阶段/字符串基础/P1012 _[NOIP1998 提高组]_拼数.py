# 回溯法

# n = input()
# l = list(input().split())

# current = []
# result = []

# def tracking(l,c,r):
#     if len(c) == len(l):
#         r.append(''.join(c))
#         return
#     for num in l:
#         if num not in c:
#             c.append(num)
#             tracking(l,c,r)
#             c.pop()

n = input()
l = list(input().split())
# result = []
max_ = [0]
def tracking(step):

    if step == len(l):
        if max_[0] < int(''.join(l)):
            max_[0] = int(''.join(l))
        return
        # result.append(''.join(l))
    for i in range(step,len(l)):
        l[step],l[i] = l[i],l[step]
        tracking(step+1)
        l[step],l[i] = l[i],l[step]
tracking(0)
print(max_[0])
# print(max(result))


from itertools import permutations
#
# n = int(input())
# l = input().split()
#
# # 使用 permutations 函数生成所有可能的排列
# perms = permutations(l)
#
# # 将排列转换为字符串，并找到最大的字符串
# max_perm = max([''.join(p) for p in perms])
#
# print(max_perm)
