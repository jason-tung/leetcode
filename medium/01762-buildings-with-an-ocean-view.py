# https://leetcode.com/problems/buildings-with-an-ocean-view/
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ret = []
        highest = 0
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > highest:
                ret.append(i)
                highest = heights[i]
        return ret[::-1]