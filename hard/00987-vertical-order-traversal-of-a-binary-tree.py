# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
        queue = [(0, 0, root.val, 0, root)]
        uuid = 1
        while len(queue):
            [depth, col, val, _, root] = heapq.heappop(queue)
            if col not in d:
                d[col] = []
            d[col].append(val)
            if root.left:
                heapq.heappush(queue, (depth+1, col-1,  root.left.val, uuid, root.left))
                uuid += 1
            if root.right:
                heapq.heappush(queue, (depth+1, col+1, root.right.val, uuid, root.right))
                uuid += 1
        return [d[key] for key in sorted(d.keys())]
        