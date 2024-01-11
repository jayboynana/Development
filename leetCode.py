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
    nums = [1, 2, 3, 4, 5, 6, 7]
    nums1 = nums.copy()
    # k=3
    # number_189(nums,k)

