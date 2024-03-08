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
                d[col] = {}
            if depth not in d[col]:
                d[col][depth] = []
            heapq.heappush(d[col][depth], root.val)
            if root.left:
                queue.appendleft((root.left, depth + 1, col-1))
            if root.right:
                queue.appendleft((root.right, depth + 1, col+1))
        ret = []
        for col in sorted(d.keys()):
            r = []
            for row in sorted(d[col].keys()):
                while len(d[col][row]):
                    r.append(heapq.heappop(d[col][row]))
            ret.append(r)
        return ret
        