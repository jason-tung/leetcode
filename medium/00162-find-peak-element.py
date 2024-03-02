# https://leetcode.com/problems/find-peak-element/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l != r:
            m = (l + r) // 2
            left_elem = nums[m-1] if m > 0 else float("-inf") 
            right_elem = nums[m+1] if m < len(nums)-1  else float("-inf") 
            if nums[m] > left_elem and nums[m] > right_elem:
                return m
            if right_elem > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return l