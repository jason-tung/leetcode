#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
        for j in range(len(s)):
            while s[j] in chars:
                chars.remove(s[i])
                i+= 1
            m = max(m, j-i+1)
            chars.add(s[j])
        i, m = 0, 0
        chars = set()
    def lengthOfLongestSubstring(self, s: str) -> int:
class Solution:
            # print(i,j,s[j], chars)
        return m