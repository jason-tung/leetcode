#https://leetcode.com/problems/coin-change-ii/description/
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # first do with o(nm) memory
        table = [[0] * (amount + 1)]*len(coins)
        for m in range(len(table)):
            for n in range(len(table[m])):
                r = 0
                # print(m,n)
                # first column shouldn't add from right
                if n != 0:
                    if n-coins[m] >= 0:
                        r += table[m][n - coins[m]]
                    # first row shouldn't add from row below it
                    if m != 0:
                        r += table[m-1][n]
                    table[m][n] = r
                else:
                    table[m][n] = 1
        # print(table)
        return table[-1][-1]
                
# edgecases: off the array -> 0
# opt(n, m-1) (no m-index coins)