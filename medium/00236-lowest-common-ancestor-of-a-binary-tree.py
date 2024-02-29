# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)  if root.left else None
        r = self.lowestCommonAncestor(root.right, p, q)  if root.right else None
        # if p and q are on split sides: return root 
        if l and r:
            return root
        # can reduce problem to subtree with both p and q on it
        return l if l else r