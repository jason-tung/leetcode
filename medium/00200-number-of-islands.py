# https://leetcode.com/problems/number-of-islands/?envType=daily-question&envId=2024-04-19
dirs = [(0,1), (0,-1), (1,0), (-1,0)]
def dfs(grid, i, j):
    grid[i][j] = "#"
    for d in dirs:
        ni, nj = d[0] + i, d[1] + j
        if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[0]) and grid[ni][nj] == "1":
            dfs(grid, ni, nj)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    c += 1
                    dfs(grid, i, j)
        return c