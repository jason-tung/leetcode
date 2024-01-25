# https://leetcode.com/problems/excel-sheet-column-title/
def helper(col, ret):
    if col == 0:
        return ret
    digit = (col - 1) % 26
    return helper((col - (digit + 1))//26, chr(ord('A')+digit) + ret)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        return helper(columnNumber, '')