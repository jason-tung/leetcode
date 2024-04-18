# https://leetcode.com/problems/island-perimeter/?envType=daily-question&envId=2024-04-18
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
        s = 0
class Solution:
                        ni, nj = i + d[0], j + d[1]
                        if ni < 0 or nj < 0 or ni>=len(grid) or nj >=len(grid[0]):
                        elif grid[ni][nj] == 0:
                    for d in dirs:
                            s += 1
                            s += 1
        return s