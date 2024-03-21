# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m, cur = float('-inf'), 0
        for k in nums:
            cur += k
            m = max(m, cur)
            if cur <= 0:
                cur = 0
        return m