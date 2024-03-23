# https://leetcode.com/problems/valid-palindrome-iii/
def solve(s, i, j, k, d):
    if i >= j:
        return True
    if (i, j, k) in d:
        return d[(i,j,k)]
    if s[i] != s[j]:
        d[(i,j,k)] =  k > 0 and (solve(s, i+1, j, k - 1, d) or solve(s, i, j-1, k-1, d))
    else:
        d[(i,j,k)] = solve(s, i+1, j-1, k, d)
    return d[(i,j,k)]
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        d = {}
        return solve(s, 0, len(s) - 1, k, d)