def isAera(nums, x, y):
    if len(nums) == 0:
        return False
    m = len(nums)
    n = len(nums[0])
    return 0 <= x < m and 0 <= y < n


def dfs(nums, x, y):
    if not isAera(nums, x, y):
        return 0
    if nums[x][y] != 1:
        return 0
    nums[x][y] = 2
    left = dfs(nums, x - 1, y)
    right = dfs(nums, x + 1, y)
    upper = dfs(nums, x, y - 1)
    down = dfs(nums, x, y + 1)
    return 1 + left + right + upper + down

#岛屿的最大的面积
def maxAreaOfIsland(grid):
    m = len(grid)
    n = len(grid[0])
    maxArea = 0
    curArea = 0
    for i in range(m):
        for j in range(n):
            curArea = dfs(grid,i,j)
            maxArea = max(curArea, maxArea)
    return maxArea


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(maxAreaOfIsland(grid))
