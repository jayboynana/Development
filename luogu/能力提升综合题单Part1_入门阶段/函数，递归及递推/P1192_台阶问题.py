# 递归超时
# 动态规划

n,k = map(int,input().split())
# def climbStairs_recursive(n, k):
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     ways = 0
#     for i in range(1, k + 1):
#         sub_ways = climbStairs_recursive(n - i, k)
#         ways += sub_ways if sub_ways is not None else 0
#     return ways
#
# c = climbStairs_recursive(n,k)
# print(c)

# def climbStairs_dp(n, k):
#     dp = [0] * (n + 1)
#     dp[0] = 1  # 初始条件，到达第0级台阶的方式数量为1
#     for i in range(1, n + 1):
#         for j in range(1, min(k, i) + 1):
#             dp[i] += dp[i - j] % 100003
#     return dp[n] % 100003
# print(climbStairs_dp(n,k))

dp = [0] * (n + 1)
dp[0],dp[1] = 1,1
for i in range(2,n+1):
    if i <= k-1:
        dp[i] = (2 * dp[i-1]) % 100003
    else:
        dp[i] = sum(dp[i-k:i]) % 100003
print(dp[n])