# https://leetcode.com/problems/summary-ranges/
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        if not(len(nums)):
            return output
        marker, last = None, None
        for i in range(len(nums)):
            num = nums[i]
            if marker == None:
                marker = num
            elif num > last + 1:
                if marker != last:
                    output.append(f"{marker}->{last}")
                else:
                    output.append(str(marker))
                marker = num
            last = num
        if marker != last:
            output.append(f"{marker}->{last}")
        else:
            output.append(str(marker))
        return output