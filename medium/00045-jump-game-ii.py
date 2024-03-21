# https://leetcode.com/problems/jump-game-ii/
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reachable = jump_limit = jumps = i = 0
        while jump_limit < len(nums) - 1:
            max_reachable = max(max_reachable, nums[i] + i)
            if i >= jump_limit or max_reachable >= len(nums) - 1:
                jumps += 1
                jump_limit = max_reachable
            i += 1
        return jumps