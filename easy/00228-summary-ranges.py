# https://leetcode.com/problems/summary-ranges/
                    output.append(str(marker))
                marker = num
            last = num
                else:
                    output.append(f"{marker}->{last}")
                if marker != last:
            elif num > last + 1:
                marker = num
            if marker == None:
        if marker != last:
            output.append(f"{marker}->{last}")
        else:
            output.append(str(marker))
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        if not(len(nums)):
            return output
        marker, last = None, None
        for i in range(len(nums)):
            num = nums[i]
        return output