# https://leetcode.com/problems/intersection-of-two-arrays/?envType=daily-question&envId=2024-03-10
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = []
        nums1.sort()
        nums2.sort()
        i, j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                r.append(nums1[i])
                while i < len(nums1) and nums1[i] == nums2[j]:
                    i += 1
            while i < len(nums1) and nums1[i] < nums2[j]:
                i += 1
            while i < len(nums1) and j < len(nums2) and nums2[j] < nums1[i]:
                j+= 1
        return r