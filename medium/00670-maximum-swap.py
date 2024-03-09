# https://leetcode.com/problems/maximum-swap/
class Solution:
    def maximumSwap(self, num: int) -> int:
        out = [int(k) for k in str(num)]
        l = [(-v, -k) for (k,v) in enumerate(out)]
        heapq.heapify(l)
        count = 0
        i = 0
        d= defaultdict(int)
        while count < 1 and i < len(out):
            pop = heapq.heappop(l)
            d[-pop[0]] = max(d[-pop[0]], -pop[1])
            while i < len(out) - 1 and out[i] == -pop[0]:
                i += 1
                pop = heapq.heappop(l)
                d[-pop[0]] = max(d[-pop[0]], -pop[1])
            if out[i] < -pop[0]:
                out[i],out[d[-pop[0]]] = out[d[-pop[0]]], out[i]
                count += 1
            i+= 1
        return int(''.join(str(x) for x in out))