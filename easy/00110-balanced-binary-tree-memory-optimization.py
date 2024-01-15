# https://leetcode.com/problems/balanced-binary-tree/
#memory optimization
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(node):
    if node == None:
        return 0
    l = helper(node.left)
    r = helper(node.right)
    if abs(l - r) > 1 or l == -1 or r == -1:
        return -1
    return max(l, r) + 1
# for root to be balanced, we check if the left and right subtrees are balanced
# reframe the problem as: find the height diff in the subtrees 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return helper(root) >= 0