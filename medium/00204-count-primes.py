# https://leetcode.com/problems/count-primes/
class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [False] * n
        c = 0
        for k in range(2,n):
            if sieve[k] == False:
                c += 1
                for j in range(2,math.ceil(n/k)):
                    sieve[k * j] = True
        return c