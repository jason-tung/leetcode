# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# testy
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r = [root.val]
        cur = root
        stack = [root]
        # groot optimization - only append useful nodes 
        while cur or len(stack) > 0:
            if cur and cur.left:
                stack.append(cur.left)
                cur = cur.left
            else:
                last = stack.pop()
                cur = last.right
                if cur:
                    stack.append(cur)
            if cur:
                r.append(cur.val)
        return r