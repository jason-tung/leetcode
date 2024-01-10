# https://leetcode.com/problems/symmetric-tree/
        return l.val == r.val
    if not l.left and not l.right and not r.right and not r.left:
        return False
    if l and not r or not l and r:
        return True
    if not l and not r:
    return l.val == r.val and isSymEqual(l.left, r.right) and isSymEqual(l.right, r.
left)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return isSymEqual(root, root)
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
 
def isSymEqual(l,r):