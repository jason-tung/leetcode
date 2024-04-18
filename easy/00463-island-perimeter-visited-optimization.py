# https://leetcode.com/problems/island-perimeter/?envType=daily-question&envId=2024-04-18
# visited optimization
dirs = [(0,1), (0,-1), (1,0), (-1,0)]
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        s = 0
        si,sj = 0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    si, sj = i, j
                    break       
            else:
                continue
            break
        queue = deque([(si, sj)])
        visited = set([(si, sj)])
        while queue:
            i, j = queue.pop()
            for d in dirs:
                ni, nj = i + d[0], j + d[1]
                if ni < 0 or nj < 0 or ni>=len(grid) or nj >=len(grid[0]):
                    s += 1
                elif grid[ni][nj] == 0:
                    s += 1
                elif (ni, nj) not in visited:
                    queue.appendleft((ni, nj))
                    visited.add((ni, nj))
        return s
    