#https://leetcode.com/problems/spiral-matrix-ii/
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0]*n for _ in range(n)]
        row, col, row_incr, col_incr, tot = 0, 0, 0, 1, 1
        while tot <= n**2:
          ret[row][col] = tot
          tot += 1
          prow = row + row_incr
          pcol = col + col_incr
          if row + row_incr >= n or prow < 0 or pcol >= n or pcol < 0 or ret[prow]
[pcol] != 0:
            col_incr, row_incr = -row_incr, col_incr
          row += row_incr
          col += col_incr
        return ret