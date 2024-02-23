# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for k in intervals[1:]:
            if k[0] <= output[-1][1]:
                output[-1][1] = max(k[1], output[-1][1])
            else:
                output.append(k)
        return output