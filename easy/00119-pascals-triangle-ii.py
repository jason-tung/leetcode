# https://leetcode.com/problems/pascals-triangle-ii/
        partial = self.getRow(rowIndex - 1)
        partial_cont = [1]
        for i in range(rowIndex - 1):
            s = partial[i] + partial[i+1]
            partial_cont.append(s)
        partial_cont.append(1)
        return partial_cont
            return [1]
        if rowIndex == 0:
    def getRow(self, rowIndex: int) -> List[int]:
class Solution: