# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return helper(s,i+1,j) or helper(s,i, j-1)
        return True
    
def helper(s,i,j):
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    return i >= j