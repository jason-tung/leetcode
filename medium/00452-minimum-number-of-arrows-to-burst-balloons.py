# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=daily-question&envId=2024-03-18
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda b: b[1])
        count, dart = 0, float('-inf')
        for i in range(len(points)):
            if not (dart >= points[i][0] and dart <= points[i][1]):
                count += 1
                dart = points[i][1]
        return count