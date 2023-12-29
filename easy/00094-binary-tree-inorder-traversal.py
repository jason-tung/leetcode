#https://leetcode.com/problems/binary-tree-inorder-traversal/description/
        while cur or len(stack) > 0:
        stack = [root]
        # groot optimization
            if cur and cur.left:
                stack.append(cur.left)
                cur = cur.left
            else:
                last = stack.pop()
                r.append(last.val)
                cur = last.right
                if cur:
                    stack.append(cur)
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r = []
        cur = root
        return r