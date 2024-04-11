# https://leetcode.com/problems/remove-k-digits/?envType=daily-question&envId=2024-04-11
                return int(res)
            res = helper(num, i + 1, k)
            res2 = helper(num, i + 1, k - 1)
            temp = num[i]
            num[i] = temp
            num[i] = ''
                res = ''.join(num)
                if not res:
                    return 0
            if k == 0 or i == len(num):
        def helper(num, i, k):
    def removeKdigits(self, num: str, k: int) -> str:
class Solution:
            return min(res, res2)
        return str(helper(list(num), 0, k))