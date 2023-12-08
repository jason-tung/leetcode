#https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        return len(s) - s.rfind(' ') - 1