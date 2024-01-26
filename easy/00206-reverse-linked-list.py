# https://leetcode.com/problems/reverse-linked-list/
# recursive
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p1, p2 = head, head.next
        p1.next = None
        while p2:
            p3 = p2.next
            p2.next = p1
            p1,p2=p2,p3
        return p1
        
        