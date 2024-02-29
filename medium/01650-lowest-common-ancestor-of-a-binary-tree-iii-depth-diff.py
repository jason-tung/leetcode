# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
# depth diff
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
        tp,tq = p,q
        dp = dq = 0
        while tp:
            dp += 1
            tp = tp.parent
        while tq:
            dq += 1
            tq = tq.parent
        while dp > dq:
            p = p.parent
            dp -= 1
        while dq > dp:
            q = q.parent
            dq -= 1
        while q != p:
            q = q.parent
            p = p.parent
        return p
        