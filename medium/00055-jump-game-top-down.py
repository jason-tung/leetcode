# https://leetcode.com/problems/jump-game/
# top down
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lowest_starting = i = len(nums) - 1
        while i >= 0:
            if nums[i] + i >= lowest_starting:
                lowest_starting = i
            i-=1
        return lowest_starting == 0