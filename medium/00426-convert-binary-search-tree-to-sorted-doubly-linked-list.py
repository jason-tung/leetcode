# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        def helper(root):
            if not root or root.left == None and root.right == None:
                return (root, root)
            l = helper(root.left) if root.left else None
            r = helper(root.right) if root.right else None
            if l:
                l[1].right = root
                root.left = l[1]
            if r:
                r[0].left = root
                root.right = r[0]
            sol = (l[0] if l else root, r[1] if r else root)
            if sol[0]:
                sol[0].left = sol[1]
            if sol[1]:
                sol[1].right = sol[0]
            return sol
        sol = helper(root)
        if sol[0] == sol[1]:
            sol[0].left = sol[0]
            sol[0].right = sol[0]
        return sol[0]