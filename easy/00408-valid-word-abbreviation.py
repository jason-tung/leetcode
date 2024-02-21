# https://leetcode.com/problems/valid-word-abbreviation/
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                digits = ''
                while j < len(abbr) and abbr[j].isdigit():
                    if len(digits) == 0 and abbr[j] == '0':
                        return False
                    digits += abbr[j]
                    j += 1
                i += int(digits)
        return i == len(word) and j == len(abbr)