# https://leetcode.com/problems/add-one-row-to-tree/?envType=daily-question&envId=2024-04-16
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.val = val
        self.depth = depth
        if depth == 1:
            return TreeNode(val, root)
        self.helper(root, None, 2)
        return root
    
    def helper(self, node, parent, curdep):
        val = self.val
        if curdep == self.depth:
            left, right = node.left, node.right
            node.left = TreeNode(val, left)
            node.right = TreeNode(val, None, right)
        else:
            self.helper(node.left, node, curdep+1) if node.left else 0
            self.helper(node.right, node, curdep+1) if node.right else 0