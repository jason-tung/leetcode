#https://leetcode.com/problems/coin-change-ii/description/
# let n be coins, m is current iteration of array
# opt(n,m) = last coin must either be accessible from an m index-coin or not.
# opt(n-coins[m], m) (using m-indexed coins)
# plus
# opt(n, m-1) (no m-index coins)
# edgecases: off the array -> 0 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # do with o(n) memory - replace table calls using m with high low
        table = [0] * (amount + 1)
        for m in range(len(coins)):
            for n in range(amount+1):
                if n != 0:
                    if n-coins[m] >= 0:
                        table[n] += table[n - coins[m]]
                else:
                    table[n] = 1
        return table[-1]
                