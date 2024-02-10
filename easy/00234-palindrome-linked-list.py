# https://leetcode.com/problems/palindrome-linked-list/
            t = t.next
        med = l // 2
        for _ in range(med):
            l += 1
            s.append(head.val)
        while t:
        t = head
        s = []
        l = 0
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
# first with unoptimized memory then opt mem
class Solution:
#         self.next = next
#     def __init__(self, val=0, next=None):
#         self.val = val
# Definition for singly-linked list.
# class ListNode:
            head = head.next
        if l % 2:
            head = head.next
        for _ in range(med):
            if head.val != s[-1]:
                return False
            s.pop()
            head = head.next
        return True