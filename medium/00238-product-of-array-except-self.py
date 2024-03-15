# https://leetcode.com/problems/product-of-array-except-self/?envType=daily-question&envId=2024-03-15
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        flip = False
        flip2 = False
        for k in nums:
            if k != 0:
                prod *= k
            elif flip:
                flip2 = True
            else:
                flip = True
        for i in range(len(nums)):
            if nums[i] == 0 and not flip2:
                nums[i] = prod
            elif not flip:
                nums[i] = prod // nums[i]
            else:
                nums[i] = 0
        return nums