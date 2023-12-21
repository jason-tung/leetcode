#https://leetcode.com/problems/sqrtx/description/
            if med*med == x:
                return med
            if med * med > x:
                high = med - 1
            else:
            med = (low + high)//2
        while low <= high:
        low, high = 0, x // 2
                low = med + 1
        # this trick works because we wait for high and low to converge and 
        # the next iteration will always set high to the solution
        # if high ** 2 > x we must decrement by 1, else we know it's the sol
        return high