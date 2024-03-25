# https://leetcode.com/problems/copy-list-with-random-pointer/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        def getOrCreate(node):
            if node:
                if node not in d:
                    new = Node(node.val)
                    d[node] = new
                return d[node]
            return None
        other = Node(0)
        anchor = other
        while head:
            other.next = getOrCreate(head)
            other = other.next
            other.random = getOrCreate(head.random)
            head = head.next
        return anchor.next