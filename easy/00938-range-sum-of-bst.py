# https://leetcode.com/problems/range-sum-of-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        ret = root.val if root.val >= low and root.val <= high else 0
        if root.left or root.right:
            if root.left and root.val >= low:
                ret += self.rangeSumBST(root.left, low, high)
            if root.right and root.val <= high:
                ret += self.rangeSumBST(root.right, low, high)
        return ret
        