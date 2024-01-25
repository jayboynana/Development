from collections import Counter
import numpy as np


def number_169(nums):
    l = len(nums)
    if l == 0:
        return 0
    my_dict = {}
    for i in nums:
        if my_dict.get(i, None):
            my_dict[i] = my_dict.get(i) + 1
        else:
            my_dict[i] = 1
    return max(my_dict, key=my_dict.get)


def number_88(nums1, m, nums2, n):
    i = j = 0
    l = []
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            l.append(nums1[i])
            i += 1
        else:
            l.append(nums2[j])
            j += 1
    while i < m:
        l.append(nums1[i])
        i += 1
    while j < n:
        l.append(nums2[j])
        j += 1
    return l


def number_189(nums, k):
    nums = nums[::-1]
    nums1 = nums[0:k][::-1]
    nums2 = nums[k:][::-1]
    nums1.extend(nums2)
    return nums1


def num_121(prices):
    inf = int(1e9)
    minprice = inf
    maxprofit = 0
    for price in prices:
        maxprofit = max(price - minprice, maxprofit)
        minprice = min(price, minprice)
    return maxprofit


def number_125(nums):
    s = nums.lower()
    s = "".join(list(map(lambda x: x if x.isalpha() or x.isdigit() else "", s)))
    if s is None or len(s) == 1:
        return False
    s1 = s[::-1]
    return s1 == s


def number_121(prices):
    if prices is None or len(prices) == 0:
        return None
    min = prices[0]
    larget = 0
    for i in range(1, len(prices)):
        if prices[i] < min:
            min = prices[i]
        if prices[i] - min > larget:
            larget = prices[i] - min
    return larget


def number_50(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / number_50(x, -n)
    # if n%2==0:
    #     return number_50(x*x,n/2)
    # return x*number_50(x,n-1) 
    if n % 2 == 0:
        half=number_50(x , n / 2)
        return half*half
    half=number_50(x, n//2)
    return half*half*x


def getValue(ch):
    if ch == 'I':
        return 1
    elif ch == "V":
        return 5


def number_13(s):
    s = s.replace(" ", "")
    char_count = Counter(s)
    my_dict = dict(char_count)
    sum = 0
    for key, value in my_dict.items():
        if key == "I":
            sum += value
        elif key == "V":
            sum += value * 5
        elif key == "X":
            sum += value * 10
        elif key == "L":
            sum += value * 50
        elif key == "C":
            sum += value * 100
        elif key == "D":
            sum += value * 500
        elif key == "M":
            sum += value * 1000
    return sum


# 给定n个整数a1,a2...an 求它们两两相乘再相加的和
def pre_sum(arr):  # 前缀和 时间复杂度o(n)
    # sum=0
    # for i in range(len(arr)-1):
    #     for j in range(i+1,len(arr)):
    #         sum+=arr[i]*arr[j]
    # return sum;
    preSum = np.zeros_like(arr)
    preSum[0] = arr[0]
    for i in range(1, len(arr)):
        preSum[i] = preSum[i - 1] + arr[i]
    sum = 0
    l = len(preSum)
    for i in range(l - 1):
        sum += arr[i] * (preSum[l - 1] - preSum[i])
    return sum

def number_133(n):
    count=0
    while n:
        count+=1
        n&=(n-1)
    return count
if __name__ == "__main__":

    # nums = [3, 3, 4]
    # n_169 = number_169(nums)
    # # print(n)
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3
    # n_88 = number_88(nums1, m, nums2, n)
    # print(n_88)
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # nums1 = nums.copy()
    # k=3
    # number_189(nums,k)
    # prices=[9,3,12,1,2,3]
    # prices=[7,6,5,4,3,2,1]
    # print(num_121(prices))
    s = "0P"
    # s.isdigit()
    # print(number_125(s))
    # print(s.isalpha())
    # nums=[7,6,4,3,1]
    # ans = number_121(nums)
    # print(ans)
    # s = "MCMXCIV"
    # ans = number_13(s)
    # print(ans)
    # arr=[1,2,3]
    # print(pre_sum(arr))
    # arr=[1,5,3,7,5]
    # diff=np.zeros_like(arr)
    # diff[0]=arr[0]
    # for i in range(1,len(arr)):
    #     diff[i]=arr[i]-arr[i-1]
    # pre_sum=np.zeros_like(diff)
    # pre_sum[0]=diff[0]
    # print(diff)
    # for i in range(1,len(diff)):
    #     pre_sum[i]=pre_sum[i-1]+diff[i]
    # print(pre_sum)
    # res = number_50(2, 10)
    # print(res)
    num = 0b00000000000000000000000000001011
    ans = number_133(num)
    print(ans)
    
    