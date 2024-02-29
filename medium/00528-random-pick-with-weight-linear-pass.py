# https://leetcode.com/problems/random-pick-with-weight/
# linear pass
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
        for i in range(len(self.w_val)):
            if rand <= self.w_val[i]:
                return i
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()