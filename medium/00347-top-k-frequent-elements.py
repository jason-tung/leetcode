#https://leetcode.com/problems/top-k-frequent-elements/description/
import heapq
# hi
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i not in counts:
                counts[i] = 0
            counts[i]+=1
        heap = [(-v,k) for k,v in counts.items()]
        heapq.heapify(heap)
        r = []
        for i in range(k):
            r.append(heapq.heappop(heap))
        return [v for k,v in r]w