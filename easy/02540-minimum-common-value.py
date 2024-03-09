# https://leetcode.com/problems/minimum-common-value/?envType=daily-question&envId=2024-03-09
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1,p2 = 0, 0
        while p1 < len(nums1) and p2<len(nums2):
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            while p1 < len(nums1) and nums1[p1] < nums2[p2]:
                p1 += 1
            while p1 < len(nums1) and p2 < len(nums2) and nums1[p1] > nums2[p2]:
                p2 += 1
        return -1