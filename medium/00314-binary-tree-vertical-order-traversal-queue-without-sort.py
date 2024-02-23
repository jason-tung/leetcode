# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# queue without sort
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue, depths = deque([(root, 0)]), {}
        mini,maxi = 0, 0
        while len(queue) > 0:
            [node, col] = queue.pop()
            if col not in depths:
                depths[col] = []
            depths[col].append(node.val)
            mini, maxi = min(col, mini), max(col, maxi)
            if node.left:
                queue.appendleft((node.left, col-1))
            if node.right:
                queue.appendleft((node.right, col+1))
        return [depths[i] for i in range(mini, maxi+1)]