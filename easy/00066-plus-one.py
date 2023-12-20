#https://leetcode.com/problems/plus-one/description/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        co = 0
        for i in range(len(digits) -1, -1, -1):
            s = co + digits[i]
            digits[i] = s % 10
            co = s // 10
        if co:
            digits.insert(0, co)
        digits[-1] += 1
        if digits[-1] <= 9:
            return digits
        return digits