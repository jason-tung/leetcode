#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      #haystack 
        for k in range(len(haystack)-len(needle)+1):
          if haystack[k:k+len(needle)] == needle:
            return k
        return -1
          