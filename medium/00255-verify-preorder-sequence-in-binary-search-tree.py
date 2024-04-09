# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/?envType=weekly-question&envId=2024-04-08
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        low = float('-inf')
        for k in preorder:
            if k < low:
                return False
            while (len(stack) and k > stack[-1]):
                low = stack.pop()
            stack.append(k)
        return True