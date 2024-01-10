# https://leetcode.com/problems/same-tree/submissions/1142802804/
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return invxor(p, q)
        left_partial, right_partial = invxor(p.left, q.left), invxor(p.right, q.right)
        if p.left and q.left:
class Solution:
            left_partial = self.isSameTree(p.left, q.left)
        if p.right and q.right:
            right_partial = self.isSameTree(p.right, q.right)
        return p.val == q.val and left_partial and right_partial