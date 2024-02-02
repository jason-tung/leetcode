# https://leetcode.com/problems/majority-element-ii/
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        return [k for k,v in counter.items() if v > len(nums) // 3]b