#https://leetcode.com/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_len = min(strs, key=len)
        i = 0
        while i < len(max_len):
            fixture = strs[0][i]
            for s in strs:
                if s[i] != fixture:
                    return s[:i]
            i+=1
        return strs[0][:i]
        