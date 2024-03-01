# 成功ac

l1 = []
l,m = map(int,input().split())
for i in range(m):
    a,b = map(int,input().split())
    l1.append({j for j in range(a,b+1)})
f = set()
# n = 0
# for v in dict1.values():
#     if not f.isdisjoint(v):
#         n = 1
#         f = f.union(v)
#     else:
#         f = f.union(v)
# if n == 1:
#     print(l - (len(f)-1) )
# else:
#     print(l-len(f)+1)
#
l += 1
for v in l1:
    f = f.union(v)
print(l-len(f))
# for k in dict1.keys():
#     for g in range(k+1,len(dict1)):
#         diff.update(dict1[k].difference(dict1[g]))
#         diff.update(dict1[g].difference(dict1[k]))
# print(len(diff))