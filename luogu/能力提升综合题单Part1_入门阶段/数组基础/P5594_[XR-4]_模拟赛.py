#

n,m,k = map(int,input().split())
c_d = []
for i in range(n):
    c_d.append([list(map(int,input().split())),0])
# print(c_d)
for i in range(1,k+1):
    s = set()
    for s_l in c_d:
        if  s_l[0]:
            if s_l[0][0] == i:
                s_l[1] += 1
                s_l[0].pop(0)
                # print(s_l)
                s.add(s_l[1])
    s = s - {0}
    print(len(s),end=' ')