# https://leetcode.com/problems/diagonal-traverse/
# using dictionary
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        store = {}
        ret = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j not in store:
                    store[i+j] = []
                store[i+j].append(mat[i][j])
        for k in sorted(store.keys()):
            ret.extend(store[k] if k%2 == 1 else store[k][::-1])
        return ret
                