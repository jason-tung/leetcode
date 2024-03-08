# https://leetcode.com/problems/diagonal-traverse/
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ret = []
        r,c = 0, 0
        dx,dy = 1,-1
        while len(ret) < len(mat) * len(mat[0]):
            ret.append(mat[r][c])
            r += dy
            c += dx
            if r >= len(mat):
                r -= 1
                c += 2
                dx, dy = 1,-1
            elif r < 0:
                r += 1
                dx, dy = -1, 1
                if c >= len(mat[0]):
                    r += 1
                    c -= 1
            elif c >= len(mat[0]):
                r += 2
                c -= 1
                dx, dy = -1, 1
            elif c < 0:
                c += 1
                dx, dy = 1, -1
        return ret
                