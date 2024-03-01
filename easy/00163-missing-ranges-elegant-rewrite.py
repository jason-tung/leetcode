# https://leetcode.com/problems/missing-ranges/
# elegant rewrite
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ret = []
        for k in nums:
            if lower!=k:
                ret.append([lower, k - 1])
            lower = k + 1
        if lower <= upper:
            ret.append([lower, upper])
        return ret