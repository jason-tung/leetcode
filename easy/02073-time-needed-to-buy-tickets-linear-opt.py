# https://leetcode.com/problems/time-needed-to-buy-tickets/?envType=daily-question&envId=2024-04-09
# linear opt
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        maxtix = tickets[k]
        for i in range(len(tickets)):
            if i <= k:
                time += min(maxtix, tickets[i])
            else:
                time += min(maxtix - 1, tickets[i])
        return time