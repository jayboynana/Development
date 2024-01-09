def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    i = j = 0
    l = []
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            l.append(nums1[i])
            i+=1
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


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    print(merge(nums1, m, nums2, n))
