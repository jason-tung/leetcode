# https://leetcode.com/problems/valid-palindrome-iii/
# top down memo
def solve(s, i, j, d):
    if i >= j:
        return 0
    if (i, j) in d:
        return d[(i,j)]
    if s[i] != s[j]:
        d[(i,j)] = min((solve(s, i+1, j, d), solve(s, i, j-1, d))) + 1
    else:
        d[(i,j)] = solve(s, i+1, j-1, d)
    return d[(i,j)]
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        d = {}
        return solve(s, 0, len(s) - 1, d) <= k