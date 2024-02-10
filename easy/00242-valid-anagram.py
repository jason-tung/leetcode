# https://leetcode.com/problems/valid-anagram/
            l[i1] += 1
            l[i2] -= 1
            i2 = ord(t[i]) - ord('a')
            if o1== 0 and l[i1] != 0:
                c += 1
            if o2 == 0 and l[i2] != 0:
            o1,o2 = l[i1],l[i2]
            elif o1 != 0 and l[i1] == 0:
                c -= 1
                c += 1
            elif o2 != 0 and l[i2] == 0:
                c -= 1 
            i1 = ord(s[i]) - ord('a')
        for i in range(len(s)):
        c = 0
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = [0]*26
            # detect state change in loop instead of doing another loop on ary
        return c == 0