# https://leetcode.com/problems/binary-subarrays-with-sum/?envType=daily-question&envId=2024-03-14
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        s = 0
        r = 0
        d = {0: 1}
        for k in nums:
            s += k
            if s - goal in d:
                r += d[s - goal]
            if s not in d:
                d[s] = 0
            d[s] += 1
        return r