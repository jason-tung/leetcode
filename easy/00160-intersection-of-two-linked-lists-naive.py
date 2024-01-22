# https://leetcode.com/problems/intersection-of-two-linked-lists/
# naive 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional
[ListNode]:
        while headA:
            b = headB
            while b:
                if b == headA:
                    return b
                b = b.next
            headA = headA.next
        return None