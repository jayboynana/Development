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
'''
git add .#添加所有更改过的文件放入暂存区
git add <指定文件名>
git commit -m ' 提交暂存区到仓库区'
git push origin <指定分支>
'''