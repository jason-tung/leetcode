# https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][0]:
            i += 1
        intervals.insert(i, newInterval)
        output = intervals[:max(1,i)]
        for k in intervals[max(1,i):]:
            if k[0] <= output[-1][1]:
                output[-1][1] = max(k[1], output[-1][1])
            else:
                output.append(k)
        return output