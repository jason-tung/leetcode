# https://leetcode.com/problems/majority-element/
            if k == m:
                c += 1
            else:
                c -= 1
            if c < 0:
                m = k
        for k in nums:
        m,c = nums[0], 0
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
                c = 1
        return m