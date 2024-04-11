# https://leetcode.com/problems/remove-k-digits/?envType=daily-question&envId=2024-04-11
# constant space
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(num)
        i = 0
        while k > 0 and i < len(num) - 1:
            temp = i
            while k > 0 and temp >= 0:
                if num[temp] != "":
                    if num[temp] <= num[i+1]:
                        break
                    num[temp] = ""
                    k -= 1
                temp -= 1
            i += 1
        while k:
            while i > 0 and not num[i]:
                i -= 1
            if i < 0:
                break
            num[i] = ""
            k -= 1
        rest = ''.join(num).lstrip('0')
        return rest if rest else "0"
            
        