# https://leetcode.com/problems/continuous-subarray-sum/
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        s = 0
        for i in range(len(nums)):
            s = (s + nums[i]) % k
            if s in d and i - d[s] >= 2:
                return True
            elif s not in d:
                d[s] = i
        return False            