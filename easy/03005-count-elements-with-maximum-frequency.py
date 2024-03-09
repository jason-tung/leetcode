# https://leetcode.com/problems/count-elements-with-maximum-frequency/?envType=daily-question&envId=2024-03-09
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        for k in nums:
            if k not in d:
                d[k] = 0
            d[k] += 1
        m, c = set(), 0
        for k in d:
            if d[k] > c:
                m = set()
                m.add(k)
                c = d[k]
            elif d[k] == c:
                m.add(k)
        c = 0
        for k in nums:
            if k in m:
                c += 1
        return c