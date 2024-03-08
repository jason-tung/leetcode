# https://leetcode.com/problems/custom-sort-string/
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        for i in range(len(order)):
            d[order[i]] = i
        return ''. join(sorted(list(s), key=lambda t: d[t] if t in d else -1))