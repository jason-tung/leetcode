# https://leetcode.com/problems/maximum-swap/
# linear opt
class Solution:
    def maximumSwap(self, num: int) -> int:
        out = [int(k) for k in str(num)]
        mx_val, mx = 0, 0
        for i in range(len(out) - 1, -1, -1):
            out[i] = (out[i], mx_val, mx)
            if out[i][0] > mx_val:
                mx = i
                mx_val = out[i][0]
        for i in range(len(out)):
            if out[i][0] < out[i][1]:
                swap = out[i][2]
                out[i],out[swap] = out[swap], out[i]
                break
        return int(''.join(str(k[0]) for k in out))