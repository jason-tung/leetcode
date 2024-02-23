# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def getWidth(root, val):
    if not (root.left or root.right):
        return val
    rv = val
    if root.left:
        rl = getWidth(root.left, [val[0]-1,val[1]-1])
        rv = [min(rl[0], rv[0]), max(rl[1], rv[1])]
    if root.right:
        rr = getWidth(root.right, [val[0]+1,val[1]+1])
        rv = [min(rr[0], rv[0]), max(rr[1], rv[1])]
    return rv
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        width = getWidth(root, [0,0])
        output = [[] for k in range(width[1] - width[0] + 1)]
        queue =  deque([(root, -width[0])])
        while len(queue) > 0:
            [node, col] = queue.pop()
            output[col].append(node.val)
            if node.left:
                queue.appendleft((node.left, col-1))
            if node.right:
                queue.appendleft((node.right, col+1))
        return output