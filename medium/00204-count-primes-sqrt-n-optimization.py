# https://leetcode.com/problems/count-primes/
# sqrt n optimization
class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [1] * n
        for k in range(min(n, 2)):
            sieve[k] = 0
        for k in range(2,int(n**.5 + 1)):
            if sieve[k] == 1:
                for j in range(2,math.ceil(n/k)):
                    sieve[k * j] = 0
        return sum(sieve)