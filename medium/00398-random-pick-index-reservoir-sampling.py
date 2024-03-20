# https://leetcode.com/problems/random-pick-index/
# reservoir sampling
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
    def pick(self, target: int) -> int:
        reser = 0
        res = -1
        for i in range(len(self.nums)):
            k = self.nums[i]
            if k == target:
                if random.randint(0,reser) == 0:
                    res = i
                reser += 1
        return res
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)