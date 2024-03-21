# https://leetcode.com/problems/meeting-rooms-ii/?envType=weekly-question&envId=2024-03-15
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key=lambda t: t[0])
        for interval in intervals:
            if len(heap) > 0 and interval[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        return len(heap)