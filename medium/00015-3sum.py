# https://leetcode.com/problems/3sum/
def twosum(target, nums, excl):
    d = {}
    r = []
    for i in range(len(nums)):
        if nums[i] not in excl:
            if target-nums[i] in d:
                r.append([target-nums[i], nums[i]])
                excl.add(target-nums[i])
                excl.add(nums[i])
            if nums[i] not in d:
                d[nums[i]] = i
    return r
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = set()
        excl = set()
        nums.sort()
        i = 0
        while i < len(nums):
            partial = twosum(-nums[i], nums[i+1:], excl.copy())
            for part in partial:
                part.append(nums[i])
                r.add(tuple(sorted(part)))
            excl.add(nums[i])
            now = nums[i]
            i+=1
            while i < len(nums) and nums[i] == now:
                i+=1
        return list(r)