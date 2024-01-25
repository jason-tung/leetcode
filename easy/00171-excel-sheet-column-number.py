# https://leetcode.com/problems/excel-sheet-column-number/
def helper(depth, col, ret):
    def titleToNumber(self, columnTitle: str) -> int:
class Solution:
    if col == '':
        return ret
    return helper(depth +1, col[:-1],ret + (ord(col[-1]) - ord('A') + 1)*26**depth)
        return helper(0, columnTitle, 0)