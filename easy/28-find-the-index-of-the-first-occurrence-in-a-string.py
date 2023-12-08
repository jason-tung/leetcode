#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      #haystack #kkk
        for k in range(len(haystack)-len(needle)+1):
          flag = True
          for i in range(len(needle)):
            flag &= haystack[k+i] == needle[i]
          if flag:
            return k
        return -1
          