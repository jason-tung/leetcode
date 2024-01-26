# https://leetcode.com/problems/reverse-linked-list/
# recursive
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def helper(node):
    if not node or not node.next:
        return node
    n = helper(node.next)
    node.next.next = node
    return n
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = helper(head)
        if r:
            head.next = None
        return r
        
        
        