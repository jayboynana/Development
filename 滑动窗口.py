# 最大子数组和
def maxSubArray(nums):
    if len(nums)==0:
        return 0
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
    return max(dp)


# 最大子数组和
def my_test(nums):
    if not nums:
        return 0

    max_sum = float('-inf')  # 初始最大和为负无穷
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# 长度最小子数组
def minSubArrayLen(target, nums):
    left = 0
    right = 0
    curSum = 0
    minLen = 0
    while right < len(nums):
        curSum += nums[right]
        while curSum >= target:
            if right - left + 1 < minLen or minLen == 0:
                minLen = right - left + 1
            curSum -= nums[left]
            left += 1
        right += 1
    return minLen

def t():
    pass
if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLen(target, nums))
    nums2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(my_test(nums2))
    nums3=[-2,1,-3,4,-1,2,1,-5,4]
    ans = maxSubArray(nums3)
    print(ans)
    
    