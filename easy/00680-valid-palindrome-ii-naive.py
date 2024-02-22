# https://leetcode.com/problems/valid-palindrome-ii/
# naive
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        for i in range(len(s)):
            ns = s[:i] + s[i+1:]
            a,b = 0, len(ns) - 1
            while a < b and ns[a] == ns[b]:
                a+=1
                b-=1
            if a >= b and ns[a] == ns[b]:
                return True
        return False