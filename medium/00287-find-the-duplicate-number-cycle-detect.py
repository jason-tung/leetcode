# https://leetcode.com/problems/find-the-duplicate-number/?envType=daily-question&envId=2024-03-24
# cycle detect
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow