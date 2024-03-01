# 未ac

n = int(input())
s = set(map(int, input().split()))
# for i in s:
#     s_diff = s - {i}
#     for j in s_diff:
#         for k in s_diff:
#             if k != j and k+j == i:
#                 c += 1
#         s_diff = s_diff - {j}
# print(c)
print(len(set(a+b for a in s for b in s if a!=b).intersection(s)))