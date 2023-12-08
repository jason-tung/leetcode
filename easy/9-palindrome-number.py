#https://leetcode.com/problems/palindrome-number/description/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0:
            return False
        build = 0
        digits = math.log10(x)//1 + 1
        for i in range(int(digits // 2)):
            build *= 10
            build+= x % 10
            x //= 10
        if digits % 2:
            x //= 10
        return build == x