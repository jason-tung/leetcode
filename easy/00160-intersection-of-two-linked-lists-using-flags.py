# https://leetcode.com/problems/intersection-of-two-linked-lists/
# using flags
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # a + c + b + c = b + c + a + c
        # a + c + b = b + c + a == node of c
        p1, p2 = headA, headB
        f1 = f2 = True
        while p1 != p2:
            if p1.next:
                p1 = p1.next
            elif f1:
                f1 = False
                p1 = headB
            else:
                return None
            if p2.next:
                p2 = p2.next
            elif f2:
                f2 = False
                p2 = headA
            else:
                return None
        return p1