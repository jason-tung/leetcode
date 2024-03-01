# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freqs = {0: 1}
        running = 0
        count = 0
        for x in nums:
            running += x
            if running - k in freqs:
                count += freqs[running - k]
            if running not in freqs:
                freqs[running] = 0
            freqs[running] += 1
        return count
            