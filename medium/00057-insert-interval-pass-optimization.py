# https://leetcode.com/problems/insert-interval/
# pass optimization
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, out = 0, []
        while i < len(intervals) and newInterval[0] >= intervals[i][0]:
            out.append(intervals[i])
            i += 1
        if len(out) > 0 and out[-1][1] >= newInterval[0]:
            out[-1][1] = max(out[-1][1], newInterval[1])
        else:
            out.append(newInterval)
        while i < len(intervals):
            if out[-1][1] >= intervals[i][0]:
                out[-1][1] = max(out[-1][1], intervals[i][1])
            else:
                out.append(intervals[i])
            i += 1
        return out
            