# https://leetcode.com/problems/reorder-list/?envType=daily-question&envId=2024-03-23
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        anchor = head
        l = 0
        while head:
            head = head.next
            l += 1
        print(l)
        head = anchor
        if l % 2:
            for k in range(l // 2):
                head = head.next
        else:
            for k in range(l // 2 - 1):
                head = head.next
        prev,cur = None, head.next
        head.next = None
        head = anchor
        while cur:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        head2 = prev
        while head2 and head:
            temp,temp2 = head.next, head2.next
            head.next = head2
            head2.next = temp
            head = temp
            head2 = temp2
            