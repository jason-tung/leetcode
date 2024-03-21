# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [rows, cols] = binaryMatrix.dimensions()
        found = False
        seek = rows - 1
        for row in range(rows):
            if binaryMatrix.get(row, seek) == 1:
                l,r = 0, seek
                while l < r:
                    m = (l + r) // 2
                    if binaryMatrix.get(row, m) == 1:
                        r = m
                    else:
                        l = m + 1
                seek = r
                found = True
        return seek if found else -1
        