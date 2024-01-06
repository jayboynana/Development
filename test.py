#冒泡排序
n=int(input())
nums=list(map(int,input().split()))
i=0
while i < n - 1:
    flag = True
    j = 0
    while j < n-i-1 :
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            flag = False
        j += 1
    if flag:
        break
    i += 1
print(*nums)
