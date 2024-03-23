# https://leetcode.com/problems/valid-palindrome-iii/
# top down memo max
def solve(s, i, j, k, d):
    if i >= j:
        return k
    if (i, j) in d:
        return d[(i,j)]
    if s[i] != s[j]:
        d[(i,j)] =\
        max((solve(s, i+1, j, k, d), solve(s, i, j-1, k, d))) - 1
    else:
        d[(i,j)] = solve(s, i+1, j-1, k, d)
    return d[(i,j)]
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        d = {}
        r = solve(s, 0, len(s) - 1, k, d)
        return r >= 0