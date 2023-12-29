#https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r = []
        cur = root
        stack = [root]
        # groot optimization 
        while cur or len(stack) > 0:
            if cur and cur.left:
                stack.append(cur.left)
                cur = cur.left
            else:
                last = stack.pop()
                r.append(last.val)
                cur = last.right
                if cur:
                    stack.append(cur)
        return r