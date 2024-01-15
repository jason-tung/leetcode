# https://leetcode.com/problems/maximum-depth-of-binary-tree/
        m = 0
        stack = [(root, 0)]
            return 0
        if not root:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
class Solution:
#         self.right = right
#         self.left = left
# stack emulation
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
        while stack:
            cur = stack.pop()
            node, val = cur[0], cur[1]
            if not node:
                m = max(val, m)
            else:
                stack.append((node.left, val + 1))
                stack.append((node.right, val + 1))
        return m
            