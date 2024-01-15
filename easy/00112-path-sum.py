# https://leetcode.com/problems/path-sum/
        r = helper(root.right, targetSum-root.val)
    if root.right:
        l = helper(root.left, targetSum-root.val)
    if root.left:
    l, r = False, False
        return targetSum == root.val
    if not root.left and not root.right:
def helper(root, targetSum):
    return l or r
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        if root == None:
            return False
        return helper(root, targetSum)