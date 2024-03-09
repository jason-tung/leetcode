# https://leetcode.com/problems/shortest-path-in-binary-matrix/
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        queue = deque([(0,0,1)])
        visited = set([(0,0)])
        while len(queue):
            [x,y,path] = queue.pop()
            if x == len(grid) - 1 and y == len(grid) -1:
                return path
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if i != 0 or j != 0:
                        dx, dy = x + i, y + j
                        if dx >= 0 and dy >= 0 and dx < len(grid) and dy < len(grid)\
                        and grid[dx][dy] == 0 and (dx,dy) not in visited:
                            queue.appendleft((dx, dy, path + 1))
                            visited.add((dx,dy))
        return -1