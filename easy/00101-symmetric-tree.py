# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# wha
def isSymEqual(l,r):
    if not l and not r:
        return True
    if l and not r or not l and r:
        return False
    if not l.left and not l.right and not r.right and not r.left:
        return l.val == r.val
    return l.val == r.val and isSymEqual(l.left, r.right) and isSymEqual(l.right, r.
left)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return isSymEqual(root, root)
            