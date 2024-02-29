# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
# looping property
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p,q
        while a != b:
            if a.parent:
                a = a.parent
            else:
                a = q
            if b.parent:
                b = b.parent
            else:
                b = p
        return a
        