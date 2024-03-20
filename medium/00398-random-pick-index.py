# https://leetcode.com/problems/random-pick-index/
class Solution:
    def __init__(self, nums: List[int]):
        self.d = {}
        for i in range(len(nums)):
            k = nums[i]
            if k not in self.d:
                self.d[k] = []
            self.d[k].append(i)
    def pick(self, target: int) -> int:
        return random.choice(self.d[target])
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)