# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        mx = 0
        while left != right:
            mx = max((right - left) * min(height[left],height[right]), mx)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return mx