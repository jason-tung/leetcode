# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/?envType=daily-question&envId=2024-03-12
# space opt
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
            s = 0 
            d = {0: ListNode(0, head)}
            anchor = d[0]
            while head: 
                s += head.val
                if s in d:
                    tempnode, temps = d[s].next, s
                    d[s].next = head.next
                    while tempnode != head:
                        temps += tempnode.val
                        del d[temps]
                        tempnode = tempnode.next
                else:
                    d[s] = head
                head = head.next
            return anchor.next
                