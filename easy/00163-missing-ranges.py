# https://leetcode.com/problems/missing-ranges/
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ret = []
        i = 0
        while i < len(nums):
            while i < len(nums) and (nums[i] <= lower or  i > 0 and nums[i] == nums[i-1]+1):
                lower = max(lower, nums[i] + 1)
                i += 1
            if i < len(nums):
                ret.append([lower, nums[i] - 1])
                lower = nums[i] + 1
                i += 1
        if lower <= upper:
            ret.append([lower, upper])
        return ret
            
    # [0,1,5,50,75]
    # 0, 99
    # [[2,4],[6,49],[51,74],[76,99]]