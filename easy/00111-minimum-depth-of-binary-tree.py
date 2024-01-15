# https://leetcode.com/problems/minimum-depth-of-binary-tree/
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = Deque([(root,1)])
        while len(queue) > 0:
            top = queue.pop()
            if not node.left and not node.right:
            [node, depth] = top
        if  not root:
            return 0
class Solution:
#         self.right = right
#         self.left = left
#         self.val = val
#     def __init__(self, val=0, left=None, right=None):
# class TreeNode:
# Definition for a binary tree node.
                return depth
            if node.left:
                queue.appendleft((node.left, depth + 1))
            if node.right:
                queue.appendleft((node.right, depth + 1))
            