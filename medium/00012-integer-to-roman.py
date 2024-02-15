# https://leetcode.com/problems/integer-to-roman/
    def intToRoman(self, num: int) -> str:
class Solution:
('IV', 4), ('I', 1)]
        i = 0
        while num > 0:
            while num >= buckets[i][1]:
        ret = []
                ret.append(buckets[i][0])
                num -= buckets[i][1]
            i += 1
buckets = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), 
('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5),
        return ''.join(ret)