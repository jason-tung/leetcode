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