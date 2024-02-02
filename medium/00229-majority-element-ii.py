# https://leetcode.com/problems/majority-element-ii/
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = None
        ct1 = ct2 = 0
        for num in nums:
            if ct1 == 0 and c2 != num:
                c1 = num
            elif ct2 == 0 and c1 != num:
                c2 = num
            if num == c1 or num == c2:
                if num == c1:
                    ct1 += 1
                else:
                    ct2 += 1
            else:
                ct1 -= 1
                ct2 -= 1
        ct1 = ct2 = 0
        for num in nums:
            if num == c1:
                ct1+=1
            if num == c2:
                ct2+= 1
        o = []
        if ct1 > len(nums)//3:
            o.append(c1)
        if ct2 > len(nums)//3:
            o.append(c2)
        return o