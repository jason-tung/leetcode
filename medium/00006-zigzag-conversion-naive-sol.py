# https://leetcode.com/problems/zigzag-conversion/
#naive sol
class Solution:
    # try to convert indicies with function after
    def convert(self, s: str, numRows: int) -> str:
        # naive sol
        if numRows == 1:
            return s
        diagonal = max(2*numRows-2, numRows)
        n = len(s) - 1
        m = [['']*((numRows-1)*(n//diagonal) + max(n%diagonal-(numRows-2),1)) for i in range(numRows)]
        n = len(s)
        i = 0
        # print(m)
        for i in range(n):
            r = 0
            if i % diagonal < numRows:
                r = i % diagonal
            else:
                r = diagonal - (i % diagonal)
            c = (numRows-1)*(i//diagonal) + max((i%diagonal)-(numRows-1),0)
            # print(i,s[i])
            # print(r, c)
            m[r][c] = s[i]
        # for k in range(numRows):
        #     print(m[k])
        return ''.join([j for k in m for j in k])