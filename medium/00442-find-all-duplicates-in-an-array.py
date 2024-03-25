# https://leetcode.com/problems/find-all-duplicates-in-an-array/?envType=daily-question&envId=2024-03-25
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ret.append(abs(num))
            nums[abs(num) - 1] *= -1
        return ret