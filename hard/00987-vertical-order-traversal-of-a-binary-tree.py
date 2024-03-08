# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
        queue = deque([(root, 0, 0)])
        while len(queue):
            [root, depth, col] = queue.pop()
            if col not in d:
                d[col] = []
            d[col].append((depth, root.val))
            if root.left:
                queue.appendleft((root.left, depth + 1, col-1))
            if root.right:
                queue.appendleft((root.right, depth + 1, col+1))
        return [[k[1] for k in sublist] for sublist in [sorted(d[key]) for key in sorted(d.keys())]]
        