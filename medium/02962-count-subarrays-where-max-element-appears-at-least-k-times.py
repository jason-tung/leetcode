# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/?envType=daily-question&envId=2024-03-29
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        ret = 0
        count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == mx:
                count += 1
            while count >= k:
                ret += len(nums) - right
                if nums[left] == mx:
                    count -= 1
                left += 1
        return ret
                