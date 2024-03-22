# https://leetcode.com/problems/remove-vowels-from-a-string/?envType=weekly-question&envId=2024-03-22
vowels = set(['a','e','i','o','u'])
class Solution:
    def removeVowels(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = ''
        return ''.join(s)