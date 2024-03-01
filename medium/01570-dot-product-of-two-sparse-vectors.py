# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.d[i] = nums[i]
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        [mind,maxd] = [self.d, vec.d] if len(self.d) <= len(vec.d) else [vec.d, self.d]
        tot = 0
        for k in mind:
            if k in maxd:
                tot += mind[k] * maxd[k]
        return tot
        
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)