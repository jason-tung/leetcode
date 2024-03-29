# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/?envType=weekly-question&envId=2024-03-29
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        maxcount, d, c = 0, defaultdict(lambda: 0), 0
        left = 0 
        for right in range(len(s)):
            d[s[right]] += 1
            if d[s[right]] == 1:
                c += 1
            if c <= k:
                maxcount = max(maxcount, right-left +1)
            while c > k:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    c -= 1
                left+=1
        return maxcount
            