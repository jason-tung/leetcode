# https://leetcode.com/problems/contiguous-array/?envType=daily-question&envId=2024-03-16
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        m = 0
        s = 0
        for i in range(len(nums)):
            k = nums[i]
            if k == 0:
                s -= 1
            else:
                s += 1
            if s in d:
                m = max(m, i - d[s])
            else:
                d[s] = i
        return m