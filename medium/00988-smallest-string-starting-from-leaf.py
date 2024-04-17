# https://leetcode.com/problems/smallest-string-starting-from-leaf/?envType=daily-question&envId=2024-04-17
            rl, rr = None, None
            if not node.left and not node.right:
                res = ''.join(chr(k + ord('a')) for k in ret)
            if node.left:
                rl = helper(node.left, ret)
            if node.right:
            ret.appendleft(node.val)
                return res
                ret.popleft()
        def helper(node, ret):
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
class Solution:
#         self.right = right
#         self.left = left
#         self.val = val
                rr = helper(node.right, ret)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
            ret.popleft()
            return min(rl, rr) if rl and rr else rl if rl else rr
        return helper(root, deque())