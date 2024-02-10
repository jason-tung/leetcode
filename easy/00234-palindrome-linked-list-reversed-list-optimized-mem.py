# https://leetcode.com/problems/palindrome-linked-list/
# reversed list optimized mem
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = 0
        t = head
        while t:
            l += 1
            t = t.next
        med = l // 2
        last = None
        for _ in range(med):
            temp = head.next
            head.next=last
            last = head
            head = temp
        if l % 2:
            head = head.next
        while head and last:
            if head.val != last.val:
                return False
            head,last=head.next,last.next
        return True