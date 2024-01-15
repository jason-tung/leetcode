# https://leetcode.com/problems/path-sum-ii/
    l, r = [], []
        return [path+[root.val]]
    if not root.left and not root.right and root.val == targetSum:
#         self.right = right
def helper(root, targetSum, path):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
# Definition for a binary tree node.
# class TreeNode:
    if root.left:
        l = helper(root.left, targetSum-root.val, path+[root.val])
    if root.right:
        r = helper(root.right, targetSum-root.val, path+[root.val])
    return l + r
class Solution:  
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        return helper(root, targetSum, [])