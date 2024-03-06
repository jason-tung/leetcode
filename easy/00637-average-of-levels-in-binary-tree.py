# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root == None:
            return []
        levels = []
        level_count = []
        def helper(node, depth):
            nonlocal levels
            nonlocal level_count
            if depth >= len(levels):
                levels.append(0)
                level_count.append(0)
            levels[depth] += node.val
            level_count[depth] += 1
            if node.left:
                helper(node.left, depth + 1)
            if node.right:
                helper(node.right, depth + 1)
        helper(root, 0)
        for i in range(len(levels)):
            levels[i] /= level_count[i]
        return levels