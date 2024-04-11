# https://leetcode.com/problems/remove-k-digits/?envType=daily-question&envId=2024-04-11
            res = helper(num, i + 1, k)
            res2 = helper(num, i + 1, k - 1)
            temp = num[i]
            num[i] = temp
            num[i] = ''
            return res if len(res) < len(res2) or len(res) == len(res2) and res < res2 else res2
                return res if res else "0"
                res = ''.join(num).lstrip("0") 
            if k == 0 or i == len(num):
        return str(helper(list(num), 0, k))
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def helper(num, i, k):