# https://leetcode.com/problems/time-needed-to-buy-tickets/?envType=daily-question&envId=2024-04-09
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = time = 0
            i = i % len(tickets)
                time += 1
            if tickets[i] != 0:
                tickets[i] -= 1
        while tickets[k] != 0:
            i += 1
        return time