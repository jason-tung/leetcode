# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new = Node(val=insertVal)
        if not head:
            new.next = new
            return new
        anchor = head
        while True:
            if head.next == anchor or\
            (head.val < insertVal and head.next.val >= insertVal or\
            (head.val > head.next.val and (head.val <= insertVal or\
            insertVal <= head.next.val))):
                new.next = head.next
                head.next = new
                return anchor
            head = head.next
        return anchor
        