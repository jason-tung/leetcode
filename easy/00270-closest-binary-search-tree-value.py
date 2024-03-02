# https://leetcode.com/problems/closest-binary-search-tree-value/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        minimized = float('inf')
        def helper(node, target):
            nonlocal minimized
            if abs(node.val - target) == abs(target - minimized):
                    minimized = min(node.val, minimized)
            elif abs(node.val - target) < abs(target - minimized):
                minimized = node.val  
            if node.left:
                helper(node.left, target)
            if node.right:
                helper(node.right, target)
        helper(root, target) 
        return minimized
        