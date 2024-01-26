# https://leetcode.com/problems/happy-number/
        slow=fast=n
    def isHappy(self, n: int) -> bool:
class Solution:
        while True:
            slow=step(slow)
            fast=step(step(fast))
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
                
# floyd cycle detect
# adding this because i had the idea and im not lazy !
def step(n):
    m = 0
    while n:
        m += (n % 10)**2
        n //= 10
    return m   