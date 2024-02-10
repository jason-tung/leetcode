# https://leetcode.com/problems/longest-palindromic-substring/
def helper(s, j, k, m):
    # print("max so far", f"_{m}_")
    while j >= 0 and k < len(s) and s[j] == s[k]:
        # print(f"executing {j}_{k}")
        if k - j + 1 > len(m):
            m = s[j:k+1]
            # print("update", f"_{m}_")
        j -= 1
        k += 1
    return m
class Solution:
    # fix the middle element of each palindrome
    def longestPalindrome(self, s: str) -> str:
        m = ''
        for i in range(len(s)):
            j = k = i
            m = helper(s,j,k, m)
        for i in range(len(s)-1):
            j,k = i, i+1
            m = helper(s,j,k, m)
        return m