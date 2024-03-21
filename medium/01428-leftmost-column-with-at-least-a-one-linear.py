# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
# linear
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
        r,c = 0, cols - 1
        ret = -1
        while r < rows and c >= 0:
            while c >= 0 and binaryMatrix.get(r,c) == 1:
                ret = c
                c -= 1
            r += 1
        return ret
        