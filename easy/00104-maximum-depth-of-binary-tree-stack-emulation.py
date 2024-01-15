# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# stack emulation
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 0)]
        m = 0
        while stack:
            cur = stack.pop()
            node, val = cur[0], cur[1]
            if not node:
                m = max(val, m)
            else:
                stack.append((node.left, val + 1))
                stack.append((node.right, val + 1))
        return m