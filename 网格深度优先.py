'''
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
'''



def isArea(nums, x, y):
    m = len(nums)
    n = len(nums[0])
    return 0 <= x < m and 0 <= y < n


def dfs(nums, x, y):
    if not isArea(nums, x, y):
        return 0
    if nums[x][y] != 1:
        return 0
    nums[x][y] = 2
    left=0
    right=0
    upper=0
    down=0
    if not isArea(nums, x-1, y)  and nums[x-1][y]==1:
        upper=1
    if not isArea(nums, x + 1, y) and nums[x + 1][y] == 1:
        down = 1
    if not isArea(nums, x, y-1) and nums[x][y-1] == 1:
        left = 1
    if not isArea(nums, x, y+1) and nums[x][y+1] == 1:
        right = 1
    return 4 - left - right - upper - down


# 岛屿的周长
def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if grid is None or len(grid)==0 or len(grid[0])==0:
        return 0
    sum = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            left=0
            right=0
            upper=0
            down=0
            if grid[i][j]==1:
                if  isArea(grid, i - 1, j) and grid[i - 1][j] == 1:
                    upper = 1
                if isArea(grid, i + 1, j) and grid[i + 1][j] == 1:
                    down = 1
                if  isArea(grid, i, j - 1) and grid[i][j - 1] == 1:
                    left = 1
                if  isArea(grid, i, j + 1) and grid[i][j + 1] == 1:
                    right = 1
                sum+=(4-left-right-upper-down)
    return sum


grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]]
# grid = [[1]]
# grid = [[1,0]]
ans = islandPerimeter(grid)
print(ans)


