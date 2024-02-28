# https://leetcode.com/problems/kth-largest-element-in-an-array/
# quick select
def partition(nums, l, r, piv):
    pivot = nums[piv]
    nums[piv], nums[r] = nums[r], nums[piv]
    next_insert = l
    for i in range(l, r):
        if nums[i] > pivot:
            nums[next_insert], nums[i] = nums[i], nums[next_insert]
            next_insert += 1
    nums[next_insert], nums[r] = nums[r], nums[next_insert]
    return next_insert
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1
        left, right = 0, len(nums) - 1
        while left != right:
            piv = random.randint(left, right)
            p = partition(nums, left, right, piv)
            if p == k:
                return nums[p]
            elif p < k:
                left = p + 1
            else:
                right = p - 1
        return nums[left]
        