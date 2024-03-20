# https://leetcode.com/problems/merge-in-between-linked-lists/?envType=daily-question&envId=2024-03-20
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l = list1
        i = 0
        while i+1 != a:
            list1 = list1.next
            i += 1
        tmp = list1
        while i-1 != b:
            list1 = list1.next
            i += 1
        tmp.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = list1
        return l