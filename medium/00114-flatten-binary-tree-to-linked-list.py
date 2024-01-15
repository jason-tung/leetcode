# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# something like this
# store ref to right child
# flatten left child and do node.right = flattened_left 
# delete left
# and move to the end of
# the ll and append right child and continue with algo
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            # print("woah", root.val)
            self.flatten(root.left)
            r = root.right
            root.right = root.left
            root.left = None
            # print(root, r)
            while root.right:
                root = root.right
            root.right = r
            # print(root)
            self.flatten(root.right)
        