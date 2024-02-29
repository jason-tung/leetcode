# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
def helper(node, p,q):
    if not node or node.val == p.val or node.val == q.val:
        return node
    l = helper(node.left, p,q) if node.left else None
    r = helper(node.right, p,q) if node.right else None
    if l and r:
        return node
    return l if l else r
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        head = p
        while head.parent:
            head = head.parent
        return helper(head, p, q)
        