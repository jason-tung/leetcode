# https://leetcode.com/problems/3sum/
# front back opt
def twosum(target, nums):
    r = []
    front, back = 0, len(nums) - 1
    while front < back:
        tot = nums[front] + nums[back]
        # print(target, nums, front, back, tot, tot == target)
        if tot > target:
            back -= 1
        elif tot < target:
            front += 1
        else:
            # print("hi")
            tf, tb = nums[front], nums[back]
            r.append([tf,tb])
            while front < back and nums[front] == tf:
                front += 1
            while front < back and nums[back] == tb:
                back -= 1
    return r
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        i = 0
        while i < len(nums):
            partial = twosum(-nums[i], nums[i+1:])
            for part in partial:
                part.append(nums[i])
                r.append(part)
            now = nums[i]
            i+=1
            while i < len(nums) and nums[i] == now:
                i+=1
        return r