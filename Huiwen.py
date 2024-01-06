n = int(input())
for i in range(10000, 999999 + 1):
    j = int(str(i)[::-1])
    if i == j:
        j = str(i)
        s = sum(map(lambda x: int(x), j))
        if s == n:
            print(i)

# s=list('123321')
# s2=sum(map(lambda x:int(x),s))
# print(s2)
