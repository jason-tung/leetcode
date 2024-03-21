# https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = i = 0
        while i < len(nums) and reachable >= i:
            reachable = max(reachable, i + nums[i])
            i+=1
        return reachable >= len(nums) - 1