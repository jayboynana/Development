def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    l = len(nums)
    if l == 0:
        return 0, nums
    i = j = 0
    while i < l:
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        i += 1
    return j, nums[0:j]


def removeDuplicates(nums):
    i = 1
    j = 0
    l = len(nums)
    if l == 0:
        return 0
    while i < l:
        if nums[i] == nums[j]:
            i += 1
        else:
            j += 1
            nums[j] = nums[i]
    return j + 1


def removeDuplicates2(nums):
    fast = 2
    slow = 2
    while fast < len(nums):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow

#为了让解法更具有一般性，我们将原问题的「保留 2 位」修改为「保留 k 位」。
def removeDuplicates2(nums,k):
    fast=k
    slow=k
    while fast<len(nums):
        if nums[fast]!=nums[slow-k]:
            nums[slow]=nums[fast]
            slow+=1
        fast+=1
    return slow
if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    # print(removeElement(nums,val))
    nums1 = [1, 1, 2]
    print(removeDuplicates(nums1))
    nums2 = [1, 1, 1, 2, 2, 3]
    l = removeDuplicates2(nums2)
    print(f"长度为:{l}")
