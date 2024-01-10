# https://leetcode.com/problems/same-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def xor(l,r):
    return l and r or not l and not r
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return xor(p, q)
        left_partial, right_partial = xor(p.left, q.left), xor(p.right, q.right)
        if p.left and q.left:
            left_partial = self.isSameTree(p.left, q.left)
        if p.right and q.right:
            right_partial = self.isSameTree(p.right, q.right)
        return p.val == q.val and left_partial and right_partial