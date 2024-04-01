# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/?envType=weekly-question&envId=2024-04-01
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = defaultdict(lambda: 0)
        left = ret = cnt = 0
        for right in range(len(s)):
            c = s[right]
            if d[c] == 0:
                cnt += 1
            d[c] += 1
            while cnt > 2:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    cnt -= 1
                left += 1
            ret = max(ret, right - left + 1)
        return ret
                