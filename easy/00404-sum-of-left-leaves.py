# https://leetcode.com/problems/sum-of-left-leaves/?envType=daily-question&envId=2024-04-14
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node, isLeft):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if isLeft else 0
            l = helper(node.left, 1) if node.left else 0
            r = helper(node.right, 0) if node.right else 0
            return l + r
        return helper(root, 0)