#https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == ' ':
          i -= 1
        marker = i
        while i>=0 and s[i] != ' ':
          i -= 1
        return marker - i