# https://leetcode.com/problems/balanced-binary-tree/
        return (0, True)
    if node == None:
def helper(node):
#         self.right = right
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
# Definition for a binary tree node.
# class TreeNode:
    l = helper(node.left)
    r = helper(node.right)
    return [max(l[0], r[0]) + 1,l[1] and r[1] and abs(l[0] - r[0]) <= 1]
# for root to be balanced, we check if the left and right subtrees are balanced
# reframe the problem as: find the height diff in the subtrees 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return helper(root)[1]