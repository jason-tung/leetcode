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
        if not head:
            return None
        dupe = Node(0)
        anchor = dupe
        while head:
            if head in d:
                dupe.next = d[head]
            else:
                dupe.next = Node(head.val)
                d[head] = dupe.next
            dupe = dupe.next
            if head.random != None:
                if head.random in d:
                    dupe.random = d[head.random]
                else:
                    dupe.random = Node(head.random.val)
                    d[head.random] = dupe.random
            head = head.next
        return anchor.next