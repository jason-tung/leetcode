# https://leetcode.com/problems/reveal-cards-in-increasing-order/?envType=daily-question&envId=2024-04-10
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        places = deque(range(len(deck)))
        res = [0 for k in range(len(deck))]
        for card in deck:
                places.append(places.popleft())
        return res
            res[places.popleft()] = card
            if places:
        deck.sort()