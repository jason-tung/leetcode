# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
            # print(root, r)
            while root.right:
                root = root.right
            root.left = None
            root.right = root.left
            r = root.right
            root.right = r
            # print(root)
            self.flatten(root.left)
            # print("woah", root.val)
            self.flatten(root.right)
        
# delete left
# and move to the end of
# the ll and append right child and continue with algo
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root: