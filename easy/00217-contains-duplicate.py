# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for k in nums:
            if k not in d:
                d[k] = 0
            else:
                return True
        return False