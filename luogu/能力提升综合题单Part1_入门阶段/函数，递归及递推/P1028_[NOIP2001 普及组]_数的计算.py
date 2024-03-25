# 超时

n = int(input())
# result = [[n]]
c = 1
def recursion(n,sub,c):

    if sub[:]:
        c += 1
        # result.append(sub[:])
        # return c
    for i in range(1,n // 2 + 1):
        sub.append(i)
        c = recursion(i,sub,c)
        sub.pop()                   
    return c
c = recursion(n,[],c)

# print(len(result))
print(c)
