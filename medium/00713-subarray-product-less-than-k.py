# https://leetcode.com/problems/subarray-product-less-than-k/?envType=daily-question&envId=2024-03-27
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        tot = 0
        prod = 1
        left = 0
        for right in range(len(nums)):
            prod *= nums[right]
            while left <= right and prod >= k:
                prod /= nums[left]
                left += 1
            if prod < k:
                tot += 1 + (right - left)
        return tot