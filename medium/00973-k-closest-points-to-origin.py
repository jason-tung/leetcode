# https://leetcode.com/problems/k-closest-points-to-origin/
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap, (-(point[0]**2 + point[1]**2), point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [k[1] for k in heap]