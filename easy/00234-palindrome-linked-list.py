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
        s = []
        while t:
            l += 1
            t = t.next
        med = l // 2
        for _ in range(med):
            s.append(head.val)
            head = head.next
        if l % 2:
            head = head.next
        for _ in range(med):
            if head.val != s[-1]:
                return False
            s.pop()
            head = head.next
        return True