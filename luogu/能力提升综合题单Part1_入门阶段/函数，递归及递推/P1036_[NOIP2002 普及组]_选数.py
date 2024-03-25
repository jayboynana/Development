# 已ac

n,k = map(int,input().split())
nums = list(map(int,input().split()))

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def cc(nums,n,k):

    result = set()
    def tracking(step,current):
        if len(current[:]) == k:
            result.add(sum(current[:]))
            # print(sum(current[:]))
            return
        for i in range(step,n):
            current.append(nums[i])
            tracking(i + 1, current)
            current.pop()

    tracking(0,[])

    c = 0
    for j in result:
        if is_prime(j):
            c += 1
    print(c)

cc(nums,n,k)