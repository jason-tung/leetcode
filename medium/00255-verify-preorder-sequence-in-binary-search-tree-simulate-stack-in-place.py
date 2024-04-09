# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/?envType=weekly-question&envId=2024-04-08
# simulate stack in place
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        i = 0
        low = float('-inf')
        for k in preorder:
            if k < low:
                return False
            while i > 0 and k > preorder[i - 1]:
                low = preorder[i - 1]
                i -= 1
            preorder[i] = k
            i += 1
        return True