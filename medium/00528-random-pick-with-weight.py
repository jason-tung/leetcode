# https://leetcode.com/problems/random-pick-with-weight/
class Solution:
    def __init__(self, w: List[int]):
        weight = sum(w)
        self.w_val = []
        tot = 0
        for k in w:
            tot += k
            self.w_val.append(tot/weight)
    def pickIndex(self) -> int:
        rand = random.random()
        l,r = 0, len(self.w_val)
        while l <= r:
            med = (l + r) // 2
            if rand <= self.w_val[med] and (med == 0 or rand > self.w_val[med - 1]):
                return med
            if rand < self.w_val[med]:
                r = med -1 
            else:
                l = med + 1
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()