# https://leetcode.com/problems/intersection-of-two-linked-lists/
        # turn it into a cycle detection problem by connecting end to head of A
        a,b = headA,headB
        if not a or not b:
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional
[ListNode]:
# clever cycle detection
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
            return None
        while a.next:
            a = a.next
        a.next = headA
        slow = fast = b
        r = None
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                r = slow
                break
        
        while r and headB != r:
            headB = headB.next
            r = r.next