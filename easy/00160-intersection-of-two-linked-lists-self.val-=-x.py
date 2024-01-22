# https://leetcode.com/problems/intersection-of-two-linked-lists/
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional
[ListNode]:
        # a + c + b + c = b + c + a + c
        # a + c + b = b + c + a == node of c
# dummy node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
        # need to insert dummy node at end to make them "equal" and terminate loop 
# without flag
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1