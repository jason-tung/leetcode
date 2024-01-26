# https://leetcode.com/problems/remove-linked-list-elements/
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional
[ListNode]:
        while head and head.next:
            if head.next and head.next.val == val:
            else:
                n = head.next
                head.next = n.next
        while head and head.val == val:
            head = head.next
        d = head
                head = head.next
        return d
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: