# https://leetcode.com/problems/pascals-triangle/
        partial = self.generate(numRows - 1)
        partial_cont = [1]
        for i in range(numRows - 2):
            s = partial[-1][i] + partial[-1][i+1]
            partial_cont.append(s)
        partial_cont.append(1)
        partial.append(partial_cont)
            return [[1]]
        return partial
        if numRows == 1:
    def generate(self, numRows: int) -> List[List[int]]:
class Solution: