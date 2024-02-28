# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-k for k in nums]
        heapq.heapify(nums)
        for i in range(k):
            if i == k - 1:
                return -heapq.heappop(nums)
            heapq.heappop(nums)