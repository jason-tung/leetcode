# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/?envType=daily-question&envId=2024-03-12
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
            s = 0 
            d = {0: ListNode(0, head)}
            anchor = d[0]
            stack = [(0,anchor)]
            while head: 
                s += head.val
                if s in d:
                    d[s].next = head.next
                    pair = stack[-1]
                    while pair[1] != d[s]:
                        del d[pair[0]]
                        stack.pop()
                        pair = stack[-1]
                else:
                    stack.append((s,head))
                    d[s] = head
                head = head.next
            return anchor.next
class Solution:
                