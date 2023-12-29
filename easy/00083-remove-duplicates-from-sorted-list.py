#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
class Solution:
#         self.next = next
        dummy = head
        while head:
            while head.next and head.val == head.next.val:
                # delete repeating nodes
                head.next = head.next.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
            head = head.next
        return dummy
        